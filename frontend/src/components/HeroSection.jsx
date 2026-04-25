import { motion } from "framer-motion";
import { ArrowRight, Clock, Sparkles, Utensils } from "lucide-react";

export default function HeroSection({ onNavigate, meals }) {
  const heroMeal = meals[0];

  return (
    <section className="relative overflow-hidden">
      <div className="section-shell grid gap-10 pb-14 pt-12 lg:grid-cols-[1.05fr_0.95fr] lg:items-center lg:pb-20 lg:pt-16">
        <motion.div initial={{ opacity: 0, y: 18 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.55 }}>
          <span className="inline-flex items-center gap-2 rounded-lg border border-orange-200 bg-white px-3 py-2 text-sm font-bold text-primary shadow-sm">
            <Sparkles size={16} />
            Startup MVP pour la FPK Khouribga
          </span>
          <h1 className="mt-6 max-w-4xl text-4xl font-black leading-tight tracking-normal text-navy sm:text-5xl lg:text-6xl">
            Commandez votre repas avant la pause. Récupérez-le sans faire la queue.
          </h1>
          <p className="mt-5 max-w-2xl text-lg leading-8 text-slate-600">
            Une solution intelligente pour les étudiants de la FPK Khouribga afin de gagner du temps, éviter le stress
            et manger mieux.
          </p>

          <div className="mt-8 flex flex-col gap-3 sm:flex-row">
            <button onClick={() => onNavigate("student")} className="primary-button">
              <Utensils size={20} />
              Commander maintenant
            </button>
            <button onClick={() => onNavigate("vendor")} className="secondary-button">
              Voir la démo
              <ArrowRight size={20} />
            </button>
          </div>

          <div className="mt-8 grid max-w-2xl gap-3 sm:grid-cols-3">
            {[
              ["12-20 min", "temps économisé"],
              ["1 MAD", "frais de service V1"],
              ["100%", "intérêt validé"],
            ].map(([value, label]) => (
              <div key={label} className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
                <p className="text-xl font-black text-navy">{value}</p>
                <p className="mt-1 text-sm text-slate-500">{label}</p>
              </div>
            ))}
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, scale: 0.96 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.1, duration: 0.6 }}
          className="relative"
        >
          <div className="overflow-hidden rounded-lg border border-white bg-white shadow-soft">
            <div className="relative h-72 sm:h-96">
              <img className="h-full w-full object-cover" src={heroMeal?.image_url} alt={heroMeal?.name || "Repas FPK"} />
              <div className="absolute inset-0 bg-gradient-to-t from-navy/80 via-navy/20 to-transparent" />
              <div className="absolute bottom-0 left-0 right-0 p-5 text-white sm:p-7">
                <div className="mb-3 inline-flex items-center gap-2 rounded-lg bg-white/15 px-3 py-2 text-sm font-semibold backdrop-blur">
                  <Clock size={16} />
                  Prêt en {heroMeal?.preparation_time || 8} min
                </div>
                <h2 className="text-2xl font-black">{heroMeal?.name || "Sandwich Poulet"}</h2>
                <p className="mt-2 max-w-md text-sm leading-6 text-white/80">
                  Préparé avant la pause, récupéré au comptoir sans perdre le temps entre deux cours.
                </p>
              </div>
            </div>
          </div>

          <div className="absolute -bottom-5 right-4 w-64 rounded-lg border border-slate-200 bg-white p-4 shadow-soft sm:right-8">
            <div className="flex items-center justify-between gap-4">
              <div>
                <p className="text-sm font-bold text-slate-500">Commande #FPK24</p>
                <p className="mt-1 text-xl font-black text-fresh">Ready</p>
              </div>
              <div className="flex h-12 w-12 items-center justify-center rounded-lg bg-emerald-50 text-fresh">
                <Utensils size={24} />
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
