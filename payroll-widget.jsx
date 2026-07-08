import React, { useState, useEffect, useMemo } from "react";
import {
  Home, Sprout, Trash2, Snowflake, Clock, Car, Sparkles,
  UtensilsCrossed, BookOpen, Boxes, Armchair, DoorOpen, X, Stamp,
  Gift, PiggyBank, Wallet, MinusCircle, CheckCircle2, CalendarPlus, Edit3
} from "lucide-react";

const C = {
  pine: "#182420",
  pineDeep: "#101B17",
  kraft: "#EAD9AE",
  kraftDark: "#DAC48F",
  ink: "#2B2620",
  inkSoft: "#5A5245",
  barn: "#9A3324",
  barnDark: "#7A2A1D",
  brass: "#B98B2A",
  chalk: "#EDE6D6",
  chalkDim: "#B9B2A2",
  line: "rgba(237,230,214,0.14)",
};

const KIDS = [
  { id: "wyatt", name: "Wyatt", age: 14 },
  { id: "molly", name: "Molly", age: 10 },
  { id: "rileigh", name: "Rileigh", age: 7 },
  { id: "cullen", name: "Cullen", age: 6 },
  { id: "emmitt", name: "Emmitt", age: 6 },
];

const JOBS = [
  { id: "coop", label: "Coop deep-clean", rate: 5, unit: "flat", icon: Home },
  { id: "garden", label: "Garden bed weeded", rate: 3, unit: "flat", icon: Sprout },
  { id: "yard", label: "Yard cleanup", rate: 1, unit: "flat", icon: Trash2 },
  { id: "snow", label: "Snow shovel", rate: 2, unit: "flat", icon: Snowflake },
  { id: "chip", label: "Wood chipping", rate: 15, unit: "hour", icon: Clock, restrictedTo: ["wyatt"] },
  { id: "vehicle", label: "Clean the car", rate: 2, unit: "flat", icon: Car },
  { id: "windows", label: "Windows, per room", rate: 1, unit: "flat", icon: Sparkles },
  { id: "drawers", label: "Kitchen drawers organized", rate: 1, unit: "flat", icon: UtensilsCrossed },
  { id: "zone-books", label: "Zone: Books & art table", rate: 2, unit: "flat", icon: BookOpen },
  { id: "zone-down", label: "Zone: Downstairs", rate: 2, unit: "flat", icon: Boxes },
  { id: "zone-common", label: "Zone: Common room", rate: 2, unit: "flat", icon: Armchair },
  { id: "mudroom", label: "Mud room reset", rate: 2, unit: "flat", icon: DoorOpen },
];

const CUSTOM_JOB = { id: "custom", label: "Something else", rate: null, unit: "custom", icon: Edit3 };

const JAR_META = [
  { key: "give", label: "Give", icon: Gift },
  { key: "save", label: "Save", icon: PiggyBank },
  { key: "spend", label: "Spend", icon: Wallet },
];

// Fixed monthly allowance, age-in-dollars, split Give/Save/Spend.
// Wyatt & Molly: Save + Spend go straight to the bank each month — only
// Give accrues here in cash. Commission still splits all three for them.
const ALLOWANCE_RATES = {
  wyatt: { give: 1, save: 3, spend: 10, trackedJars: ["give", "save", "spend"], bankPaid: ["save", "spend"] },
  molly: { give: 1, save: 2, spend: 7, trackedJars: ["give", "save", "spend"], bankPaid: ["save", "spend"] },
  rileigh: { give: 1, save: 1, spend: 5, trackedJars: ["give", "save", "spend"], bankPaid: [] },
  cullen: { give: 1, save: 1, spend: 4, trackedJars: ["give", "save", "spend"], bankPaid: [] },
  emmitt: { give: 1, save: 1, spend: 4, trackedJars: ["give", "save", "spend"], bankPaid: [] },
};
const ratioFor = (kidId) => {
  const r = ALLOWANCE_RATES[kidId];
  const total = r.give + r.save + r.spend;
  return { give: r.give / total, save: r.save / total, spend: r.spend / total };
};

const ENTRIES_KEY = "commission_entries_v1";
const CATEGORY_KEY = "money_categories_v1";
const todayStr = () => new Date().toISOString().slice(0, 10);
const monthKey = (d) => d.slice(0, 7);
const monthLabel = (mk) => {
  const [y, m] = mk.split("-").map(Number);
  return new Date(y, m - 1, 1).toLocaleString("default", { month: "long", year: "numeric" });
};

// Seed reflects the real May+June backlog as of 2026-07-04.
const SEED_CATEGORIES = {
  totals: {
    wyatt: { give: 2, save: 0, spend: 0 },
    molly: { give: 2, save: 0, spend: 0 },
    rileigh: { give: 2, save: 2, spend: 10 },
    cullen: { give: 2, save: 2, spend: 8 },
    emmitt: { give: 2, save: 2, spend: 8 },
  },
  log: [],
  lastAccrualMonth: "2026-06",
  lastPayoutMonth: {},
};

export default function Payroll() {
  const [tab, setTab] = useState("board");
  const [entries, setEntries] = useState(null);
  const [categories, setCategories] = useState(null);
  const [error, setError] = useState(null);

  const [mode, setMode] = useState("job");
  const [selectedKid, setSelectedKid] = useState(null);
  const [selectedJob, setSelectedJob] = useState(null);
  const [hours, setHours] = useState("");
  const [customLabel, setCustomLabel] = useState("");
  const [customAmount, setCustomAmount] = useState("");
  const [date, setDate] = useState(todayStr());
  const [deductAmount, setDeductAmount] = useState("");
  const [deductNote, setDeductNote] = useState("");
  const [stampFlash, setStampFlash] = useState(false);

  useEffect(() => {
    (async () => {
      try {
        const res = await window.storage.get(ENTRIES_KEY, false);
        setEntries(res ? JSON.parse(res.value) : []);
      } catch {
        setEntries([]);
      }
      try {
        const res = await window.storage.get(CATEGORY_KEY, false);
        setCategories(res ? JSON.parse(res.value) : SEED_CATEGORIES);
      } catch {
        setCategories(SEED_CATEGORIES);
      }
    })();
  }, []);

  const persistEntries = async (next) => {
    setEntries(next);
    try {
      const ok = await window.storage.set(ENTRIES_KEY, JSON.stringify(next), false);
      if (!ok) setError("Couldn't save — try again.");
    } catch {
      setError("Couldn't save — try again.");
    }
  };

  const persistCategories = async (next) => {
    setCategories(next);
    try {
      const ok = await window.storage.set(CATEGORY_KEY, JSON.stringify(next), false);
      if (!ok) setError("Couldn't save — try again.");
    } catch {
      setError("Couldn't save — try again.");
    }
  };

  const jobsForKid = (kidId) => [...JOBS.filter((j) => !j.restrictedTo || j.restrictedTo.includes(kidId)), CUSTOM_JOB];

  const computedAmount = useMemo(() => {
    if (mode !== "job" || !selectedJob) return 0;
    if (selectedJob.id === "custom") {
      const a = parseFloat(customAmount);
      return isNaN(a) ? 0 : +a.toFixed(2);
    }
    if (selectedJob.unit === "hour") {
      const h = parseFloat(hours);
      return isNaN(h) ? 0 : +(h * selectedJob.rate).toFixed(2);
    }
    return selectedJob.rate;
  }, [mode, selectedJob, hours, customAmount]);

  const canSubmitJob = selectedKid && selectedJob && (
    selectedJob.id === "custom" ? (customLabel.trim() && parseFloat(customAmount) > 0)
    : (selectedJob.unit === "flat" || parseFloat(hours) > 0)
  );
  const canSubmitDeduct = selectedKid && parseFloat(deductAmount) > 0;

  const logTicket = async () => {
    if (!canSubmitJob || !entries) return;
    const isCustom = selectedJob.id === "custom";
    const entry = {
      id: `${Date.now()}-${Math.random().toString(36).slice(2, 7)}`,
      kidId: selectedKid, type: "job", jobId: selectedJob.id,
      label: isCustom ? customLabel.trim() : selectedJob.label,
      rate: isCustom ? null : selectedJob.rate, unit: isCustom ? "custom" : selectedJob.unit,
      hours: (!isCustom && selectedJob.unit === "hour") ? parseFloat(hours) : null,
      amount: computedAmount, date,
    };
    await persistEntries([entry, ...entries]);
    setStampFlash(true);
    setTimeout(() => setStampFlash(false), 420);
    setSelectedJob(null);
    setHours("");
    setCustomLabel("");
    setCustomAmount("");
    setDate(todayStr());
  };

  const logDeduction = async () => {
    if (!canSubmitDeduct || !entries) return;
    const entry = {
      id: `${Date.now()}-${Math.random().toString(36).slice(2, 7)}`,
      kidId: selectedKid, type: "deduct", label: deductNote.trim() || "Attitude deduction",
      amount: +parseFloat(deductAmount).toFixed(2), date,
    };
    await persistEntries([entry, ...entries]);
    setStampFlash(true);
    setTimeout(() => setStampFlash(false), 420);
    setDeductAmount("");
    setDeductNote("");
    setDate(todayStr());
  };

  const deleteEntry = async (id) => {
    if (!entries) return;
    await persistEntries(entries.filter((e) => e.id !== id));
  };

  const netForMonth = (kidId, mk) => {
    if (!entries) return 0;
    let net = 0;
    for (const e of entries) {
      if (e.kidId !== kidId || monthKey(e.date) !== mk) continue;
      net += e.type === "deduct" ? -e.amount : e.amount;
    }
    return +net.toFixed(2);
  };

  const sortedEntries = entries ? [...entries].sort((a, b) => (a.date < b.date ? 1 : a.date > b.date ? -1 : 0)) : [];
  const currentMonth = monthKey(todayStr());
  const alreadyAccrued = categories?.lastAccrualMonth === currentMonth;

  const addThisMonth = async () => {
    if (!categories || alreadyAccrued) return;
    const nextTotals = { ...categories.totals };
    const adds = [];
    for (const k of KIDS) {
      const rate = ALLOWANCE_RATES[k.id];
      const bal = { ...nextTotals[k.id] };
      for (const jar of rate.trackedJars) bal[jar] = +(bal[jar] + rate[jar]).toFixed(2);
      nextTotals[k.id] = bal;
      adds.push({ id: `${Date.now()}-${k.id}-accrue`, kidId: k.id, type: "accrue", note: `${monthLabel(currentMonth)} allowance added`, date: todayStr() });
    }
    await persistCategories({ ...categories, totals: nextTotals, log: [...adds, ...categories.log], lastAccrualMonth: currentMonth });
  };

  const runPayout = async (kidId) => {
    if (!categories) return;
    const net = Math.max(0, netForMonth(kidId, currentMonth));
    if (net <= 0 || categories.lastPayoutMonth[kidId] === currentMonth) return;
    const ratio = ratioFor(kidId);
    const give = +(net * ratio.give).toFixed(2);
    const save = +(net * ratio.save).toFixed(2);
    const spend = +(net - give - save).toFixed(2);
    const prev = categories.totals[kidId];
    const nextTotals = {
      ...categories.totals,
      [kidId]: { give: +(prev.give + give).toFixed(2), save: +(prev.save + save).toFixed(2), spend: +(prev.spend + spend).toFixed(2) },
    };
    const entry = {
      id: `${Date.now()}-${kidId}-payout`, kidId, type: "payout",
      note: `${monthLabel(currentMonth)} commission — Give $${give.toFixed(2)}, Save $${save.toFixed(2)}, Spend $${spend.toFixed(2)}`,
      date: todayStr(),
    };
    await persistCategories({ ...categories, totals: nextTotals, log: [entry, ...categories.log], lastPayoutMonth: { ...categories.lastPayoutMonth, [kidId]: currentMonth } });
  };

  const runPayoutAll = async () => {
    for (const k of KIDS) {
      const net = Math.max(0, netForMonth(k.id, currentMonth));
      if (net > 0 && categories.lastPayoutMonth[k.id] !== currentMonth) await runPayout(k.id);
    }
  };

  return (
    <div style={{ backgroundColor: C.pine, minHeight: "100vh", fontFamily: "system-ui, -apple-system, sans-serif" }} className="p-4 sm:p-8">
      <style>{`
        @media (prefers-reduced-motion: no-preference) {
          .stamp-anim { animation: stampIn 0.42s cubic-bezier(.34,1.56,.64,1); }
        }
        @keyframes stampIn {
          0% { transform: scale(2.2) rotate(-14deg); opacity: 0; }
          60% { transform: scale(0.95) rotate(-6deg); opacity: 1; }
          100% { transform: scale(1) rotate(-6deg); opacity: 1; }
        }
        .ticket-focus:focus-visible { outline: 2px solid ${C.brass}; outline-offset: 2px; }
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-thumb { background: ${C.line}; border-radius: 4px; }
      `}</style>

      <div className="max-w-2xl mx-auto">
        <div className="mb-6">
          <div className="text-xs font-bold tracking-widest uppercase mb-1" style={{ color: C.brass, letterSpacing: "0.18em" }}>Punch List · Payroll</div>
          <h1 className="text-3xl sm:text-4xl font-black uppercase leading-none mb-2" style={{ color: C.chalk, letterSpacing: "-0.01em" }}>Payroll</h1>
          <p className="text-sm" style={{ color: C.chalkDim }}>Fixed allowance every month. Commission's extra, on top.</p>
          <p className="text-xs mt-0.5" style={{ color: C.chalkDim, opacity: 0.75 }}>Commission work is optional. A job worth doing is worth doing right.</p>
        </div>

        <div className="flex gap-2 mb-6">
          {[{ id: "log", label: "Log a Job" }, { id: "board", label: "Earnings Board" }, { id: "payout", label: "Payout" }].map((t) => (
            <button key={t.id} onClick={() => setTab(t.id)}
              className="ticket-focus flex-1 py-2.5 px-2 rounded-md text-xs sm:text-sm font-bold uppercase tracking-wide transition-colors"
              style={{ backgroundColor: tab === t.id ? C.brass : "transparent", color: tab === t.id ? C.pineDeep : C.chalkDim, border: `1px solid ${tab === t.id ? C.brass : C.line}` }}>
              {t.label}
            </button>
          ))}
        </div>

        {entries === null || categories === null ? (
          <div className="text-center py-16" style={{ color: C.chalkDim }}>Loading the board…</div>
        ) : tab === "log" ? (
          <LogTab {...{
            mode, setMode,
            selectedKid, setSelectedKid: (id) => { setSelectedKid(id); setSelectedJob(null); setHours(""); setCustomLabel(""); setCustomAmount(""); },
            selectedJob, setSelectedJob, hours, setHours, date, setDate, jobsForKid,
            customLabel, setCustomLabel, customAmount, setCustomAmount,
            computedAmount, canSubmitJob, canSubmitDeduct, logTicket, logDeduction,
            deductAmount, setDeductAmount, deductNote, setDeductNote,
            stampFlash, sortedEntries, deleteEntry,
          }} />
        ) : tab === "board" ? (
          <EarningsBoard {...{ categories, netForMonth, currentMonth }} />
        ) : (
          <PayoutTab {...{ categories, netForMonth, currentMonth, runPayout, runPayoutAll, addThisMonth, alreadyAccrued }} />
        )}

        {error && <div className="mt-4 text-sm text-center py-2 rounded-md" style={{ backgroundColor: C.barnDark, color: C.chalk }}>{error}</div>}
      </div>
    </div>
  );
}

function TicketCard({ children, style }) {
  return (
    <div className="rounded-lg p-5" style={{ backgroundColor: C.kraft, boxShadow: "0 4px 14px rgba(0,0,0,0.35)", border: `1px solid ${C.kraftDark}`, ...style }}>
      {children}
    </div>
  );
}

function LogTab({ mode, setMode, selectedKid, setSelectedKid, selectedJob, setSelectedJob, hours, setHours, date, setDate, jobsForKid, customLabel, setCustomLabel, customAmount, setCustomAmount, computedAmount, canSubmitJob, canSubmitDeduct, logTicket, logDeduction, deductAmount, setDeductAmount, deductNote, setDeductNote, stampFlash, sortedEntries, deleteEntry }) {
  return (
    <div className="space-y-5">
      <div className="flex gap-2">
        {[{ id: "job", label: "Job" }, { id: "deduct", label: "Deduction" }].map((m) => (
          <button key={m.id} onClick={() => setMode(m.id)}
            className="ticket-focus flex-1 py-2 rounded-md text-xs font-bold uppercase tracking-wide"
            style={{ backgroundColor: mode === m.id ? (m.id === "deduct" ? C.barn : C.brass) : "transparent", color: mode === m.id ? C.chalk : C.chalkDim, border: `1px solid ${mode === m.id ? (m.id === "deduct" ? C.barn : C.brass) : C.line}` }}>
            {m.label}
          </button>
        ))}
      </div>

      <TicketCard>
        <div className="text-xs font-bold uppercase tracking-wider mb-2" style={{ color: C.inkSoft }}>
          {mode === "job" ? "Who did the work?" : "Who's getting the deduction?"}
        </div>
        <div className="grid grid-cols-5 gap-2 mb-5">
          {KIDS.map((k) => (
            <button key={k.id} onClick={() => setSelectedKid(k.id)}
              className="ticket-focus py-2 rounded-md text-xs font-bold uppercase transition-colors"
              style={{ backgroundColor: selectedKid === k.id ? C.barn : C.kraftDark, color: selectedKid === k.id ? C.chalk : C.ink }}>
              {k.name}
            </button>
          ))}
        </div>

        {mode === "job" && selectedKid && (
          <>
            <div className="text-xs font-bold uppercase tracking-wider mb-2" style={{ color: C.inkSoft }}>Which job?</div>
            <div className="grid grid-cols-2 gap-2 mb-4">
              {jobsForKid(selectedKid).map((j) => {
                const Icon = j.icon;
                const active = selectedJob?.id === j.id;
                return (
                  <button key={j.id} onClick={() => setSelectedJob(j)}
                    className="ticket-focus flex items-center gap-2 py-2.5 px-3 rounded-md text-left transition-colors"
                    style={{ backgroundColor: active ? C.barn : "rgba(43,38,32,0.06)", border: `1px solid ${active ? C.barn : C.kraftDark}` }}>
                    <Icon size={16} color={active ? C.chalk : C.ink} strokeWidth={2} />
                    <span className="text-xs font-semibold leading-tight" style={{ color: active ? C.chalk : C.ink }}>
                      {j.label}
                      <span className="block font-normal opacity-80">
                        {j.id === "custom" ? "Set your own" : `$${j.rate}${j.unit === "hour" ? "/hr" : ""}`}
                      </span>
                    </span>
                  </button>
                );
              })}
            </div>
            {selectedJob?.unit === "hour" && (
              <div className="mb-4">
                <label className="text-xs font-bold uppercase tracking-wider block mb-1" style={{ color: C.inkSoft }}>Hours worked</label>
                <input type="number" min="0" step="0.25" value={hours} onChange={(e) => setHours(e.target.value)}
                  className="ticket-focus w-full py-2 px-3 rounded-md text-sm"
                  style={{ backgroundColor: C.chalk, color: C.ink, border: `1px solid ${C.kraftDark}` }} placeholder="e.g. 1.5" />
              </div>
            )}

            {selectedJob?.id === "custom" && (
              <div className="grid grid-cols-2 gap-2 mb-4">
                <input type="text" value={customLabel} onChange={(e) => setCustomLabel(e.target.value)}
                  placeholder="What was the job?" className="ticket-focus py-2 px-3 rounded-md text-sm"
                  style={{ backgroundColor: C.chalk, color: C.ink, border: `1px solid ${C.kraftDark}` }} />
                <input type="number" min="0" step="0.25" value={customAmount} onChange={(e) => setCustomAmount(e.target.value)}
                  placeholder="Amount" className="ticket-focus py-2 px-3 rounded-md text-sm"
                  style={{ backgroundColor: C.chalk, color: C.ink, border: `1px solid ${C.kraftDark}` }} />
              </div>
            )}
          </>
        )}

        {mode === "deduct" && selectedKid && (
          <div className="grid grid-cols-2 gap-2 mb-4">
            <input type="number" min="0" step="0.25" value={deductAmount} onChange={(e) => setDeductAmount(e.target.value)}
              placeholder="Amount" className="ticket-focus py-2 px-3 rounded-md text-sm"
              style={{ backgroundColor: C.chalk, color: C.ink, border: `1px solid ${C.kraftDark}` }} />
            <input type="text" value={deductNote} onChange={(e) => setDeductNote(e.target.value)}
              placeholder="Reason (optional)" className="ticket-focus py-2 px-3 rounded-md text-sm"
              style={{ backgroundColor: C.chalk, color: C.ink, border: `1px solid ${C.kraftDark}` }} />
          </div>
        )}

        {selectedKid && (mode === "job" ? selectedJob : true) && (
          <div className="mb-4">
            <label className="text-xs font-bold uppercase tracking-wider block mb-1" style={{ color: C.inkSoft }}>Date</label>
            <input type="date" value={date} onChange={(e) => setDate(e.target.value)}
              className="ticket-focus w-full py-2 px-3 rounded-md text-sm"
              style={{ backgroundColor: C.chalk, color: C.ink, border: `1px solid ${C.kraftDark}` }} />
          </div>
        )}

        <div className="flex items-center justify-between pt-2" style={{ borderTop: `1px dashed ${C.kraftDark}` }}>
          <div>
            <div className="text-xs uppercase font-bold tracking-wider" style={{ color: C.inkSoft }}>Amount</div>
            <div className="text-2xl font-black" style={{ color: mode === "deduct" ? C.barn : C.ink, fontFamily: "ui-monospace, Consolas, monospace" }}>
              {mode === "deduct" ? "−" : ""}${(mode === "deduct" ? (parseFloat(deductAmount) || 0) : computedAmount).toFixed(2)}
            </div>
          </div>
          {mode === "job" ? (
            <button onClick={logTicket} disabled={!canSubmitJob}
              className="ticket-focus flex items-center gap-2 py-3 px-5 rounded-md font-bold uppercase text-sm tracking-wide transition-opacity"
              style={{ backgroundColor: C.brass, color: C.pineDeep, opacity: canSubmitJob ? 1 : 0.4, cursor: canSubmitJob ? "pointer" : "not-allowed" }}>
              <Stamp size={16} /> Stamp It
            </button>
          ) : (
            <button onClick={logDeduction} disabled={!canSubmitDeduct}
              className="ticket-focus flex items-center gap-2 py-3 px-5 rounded-md font-bold uppercase text-sm tracking-wide transition-opacity"
              style={{ backgroundColor: C.barn, color: C.chalk, opacity: canSubmitDeduct ? 1 : 0.4, cursor: canSubmitDeduct ? "pointer" : "not-allowed" }}>
              <MinusCircle size={16} /> Deduct
            </button>
          )}
        </div>
      </TicketCard>

      <div>
        <div className="text-xs font-bold uppercase tracking-wider mb-2" style={{ color: C.chalkDim }}>Recent tickets</div>
        {sortedEntries.length === 0 ? (
          <div className="text-sm py-6 text-center" style={{ color: C.chalkDim }}>Nothing logged yet — the first one's on the board above.</div>
        ) : (
          <div className="space-y-2">
            {sortedEntries.slice(0, 12).map((e, i) => {
              const kid = KIDS.find((k) => k.id === e.kidId);
              const isDeduct = e.type === "deduct";
              return (
                <div key={e.id} className={`flex items-center justify-between py-2.5 px-3 rounded-md ${i === 0 && stampFlash ? "stamp-anim" : ""}`}
                  style={{ backgroundColor: "rgba(234,217,174,0.08)", border: `1px solid ${C.line}` }}>
                  <div>
                    <span className="text-sm font-bold" style={{ color: C.chalk }}>{kid?.name}</span>
                    <span className="text-sm mx-1.5" style={{ color: C.chalkDim }}>·</span>
                    <span className="text-sm" style={{ color: C.chalkDim }}>{e.label}</span>
                    <div className="text-xs mt-0.5" style={{ color: C.chalkDim, opacity: 0.7 }}>{e.date}{e.hours ? ` · ${e.hours}hr` : ""}</div>
                  </div>
                  <div className="flex items-center gap-3">
                    <span className="text-sm font-bold" style={{ color: isDeduct ? "#D4694F" : C.brass, fontFamily: "ui-monospace, Consolas, monospace" }}>
                      {isDeduct ? "−" : ""}${e.amount.toFixed(2)}
                    </span>
                    <button onClick={() => deleteEntry(e.id)} className="ticket-focus opacity-60 hover:opacity-100" aria-label={`Remove ${kid?.name} entry`}>
                      <X size={14} color={C.chalkDim} />
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}

function EarningsBoard({ categories, netForMonth, currentMonth }) {
  return (
    <div className="space-y-3">
      {KIDS.map((k) => {
        const net = Math.max(0, netForMonth(k.id, currentMonth));
        const totals = categories.totals[k.id];
        const rate = ALLOWANCE_RATES[k.id];
        return (
          <TicketCard key={k.id}>
            <div className="text-sm font-bold uppercase tracking-wide mb-3" style={{ color: C.ink }}>{k.name}</div>
            <div className="flex items-center justify-between flex-wrap gap-3">
              <div>
                <div className="text-xs font-bold uppercase" style={{ color: C.inkSoft }}>This month</div>
                <div className="text-2xl font-black" style={{ color: C.barn, fontFamily: "ui-monospace, Consolas, monospace" }}>${net.toFixed(2)}</div>
              </div>
              <div className="flex gap-3">
                {JAR_META.map((j) => {
                  const Icon = j.icon;
                  return (
                    <div key={j.key} className="text-center">
                      <Icon size={13} color={C.inkSoft} className="mx-auto mb-0.5" />
                      <div className="text-xs font-bold" style={{ color: C.inkSoft }}>{j.label}</div>
                      <div className="text-sm font-black" style={{ color: C.ink, fontFamily: "ui-monospace, Consolas, monospace" }}>${totals[j.key].toFixed(2)}</div>
                    </div>
                  );
                })}
              </div>
            </div>
            {rate.bankPaid.length > 0 && (
              <div className="text-xs mt-2 opacity-70" style={{ color: C.inkSoft }}>
                Fixed {rate.bankPaid.join(" & ")} still pays out to the bank each month — tracked here too so commission adds up right.
              </div>
            )}
          </TicketCard>
        );
      })}

      <div>
        <div className="text-xs font-bold uppercase tracking-wider mb-2" style={{ color: C.chalkDim }}>Rate card</div>
        <TicketCard>
          <div className="grid grid-cols-2 gap-x-4 gap-y-1.5">
            {JOBS.map((j) => (
              <div key={j.id} className="flex justify-between text-xs">
                <span style={{ color: C.ink }} className="opacity-80">{j.label}{j.restrictedTo ? " *" : ""}</span>
                <span style={{ color: C.inkSoft }} className="font-semibold">${j.rate}{j.unit === "hour" ? "/hr" : ""}</span>
              </div>
            ))}
          </div>
          <div className="text-xs mt-2 opacity-60" style={{ color: C.inkSoft }}>* Wyatt only</div>
          <div className="text-xs mt-2 pt-2 opacity-70" style={{ color: C.inkSoft, borderTop: `1px dashed ${C.kraftDark}` }}>
            Not up to Al's standards? I don't think so, Tim. No stamp, no pay.
          </div>
        </TicketCard>
      </div>
    </div>
  );
}

function PayoutTab({ categories, netForMonth, currentMonth, runPayout, runPayoutAll, addThisMonth, alreadyAccrued }) {
  const anyPending = KIDS.some((k) => Math.max(0, netForMonth(k.id, currentMonth)) > 0 && categories.lastPayoutMonth[k.id] !== currentMonth);
  return (
    <div className="space-y-5">
      <TicketCard>
        <div className="flex items-center justify-between">
          <div>
            <div className="text-xs font-bold uppercase tracking-wider" style={{ color: C.inkSoft }}>Fixed monthly allowance</div>
            <div className="text-sm" style={{ color: C.ink }}>{monthLabel(currentMonth)}</div>
          </div>
          <button onClick={addThisMonth} disabled={alreadyAccrued}
            className="ticket-focus flex items-center gap-2 py-2.5 px-4 rounded-md font-bold uppercase text-xs tracking-wide"
            style={{ backgroundColor: C.brass, color: C.pineDeep, opacity: alreadyAccrued ? 0.4 : 1, cursor: alreadyAccrued ? "not-allowed" : "pointer" }}>
            <CalendarPlus size={14} /> {alreadyAccrued ? "Already added" : "Add this month"}
          </button>
        </div>
      </TicketCard>

      <TicketCard>
        <div className="flex items-center justify-between">
          <div>
            <div className="text-xs font-bold uppercase tracking-wider" style={{ color: C.inkSoft }}>Commission payout</div>
            <div className="text-sm" style={{ color: C.ink }}>Splits net earnings into the jars, then zeroes the month</div>
          </div>
          <button onClick={runPayoutAll} disabled={!anyPending}
            className="ticket-focus flex items-center gap-2 py-2.5 px-4 rounded-md font-bold uppercase text-xs tracking-wide"
            style={{ backgroundColor: C.brass, color: C.pineDeep, opacity: anyPending ? 1 : 0.4, cursor: anyPending ? "pointer" : "not-allowed" }}>
            <CheckCircle2 size={14} /> Run all
          </button>
        </div>
      </TicketCard>

      <div className="space-y-2">
        {KIDS.map((k) => {
          const net = Math.max(0, netForMonth(k.id, currentMonth));
          const done = categories.lastPayoutMonth[k.id] === currentMonth;
          const ratio = ratioFor(k.id);
          return (
            <TicketCard key={k.id}>
              <div className="flex items-center justify-between mb-2">
                <span className="text-sm font-bold uppercase" style={{ color: C.ink }}>{k.name}</span>
                <span className="text-lg font-black" style={{ color: C.barn, fontFamily: "ui-monospace, Consolas, monospace" }}>${net.toFixed(2)}</span>
              </div>
              <div className="flex items-center justify-between">
                <div className="text-xs" style={{ color: C.inkSoft }}>
                  Give {Math.round(ratio.give * 100)}% · Save {Math.round(ratio.save * 100)}% · Spend {Math.round(ratio.spend * 100)}%
                </div>
                <button onClick={() => runPayout(k.id)} disabled={net <= 0 || done}
                  className="ticket-focus flex items-center gap-1 py-1.5 px-3 rounded text-xs font-bold uppercase"
                  style={{ backgroundColor: done ? "transparent" : C.ink, color: done ? C.inkSoft : C.kraft, opacity: (net <= 0 || done) ? 0.5 : 1 }}>
                  {done ? "Paid" : "Run"}
                </button>
              </div>
            </TicketCard>
          );
        })}
      </div>

      <div>
        <div className="text-xs font-bold uppercase tracking-wider mb-2" style={{ color: C.chalkDim }}>Recent activity</div>
        {categories.log.length === 0 ? (
          <div className="text-sm py-4 text-center" style={{ color: C.chalkDim }}>Nothing logged yet.</div>
        ) : (
          <div className="space-y-1.5">
            {categories.log.slice(0, 10).map((l) => {
              const kid = KIDS.find((k) => k.id === l.kidId);
              return (
                <div key={l.id} className="py-2 px-3 rounded-md text-xs" style={{ backgroundColor: "rgba(234,217,174,0.08)", border: `1px solid ${C.line}` }}>
                  <span className="font-bold" style={{ color: C.chalk }}>{kid?.name}</span>
                  <span style={{ color: C.chalkDim }}> · {l.note}</span>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}
