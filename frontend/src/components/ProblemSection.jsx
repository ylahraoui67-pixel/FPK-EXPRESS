import { motion } from "framer-motion";
import { Clock3, HeartPulse, ShieldAlert, WalletCards } from "lucide-react";

const problems = [
  {
    title: "Files longues",
    text: "Plus de 81% des étudiants attendent 15 minutes ou plus pour acheter à manger ou un café.",
    icon: Clock3,
  },
  {
    title: "Repas sautés",
    text: "Environ 95% sautent parfois un repas ou mangent mal pour éviter d'arriver en retard.",
    icon: HeartPulse,
  },
  {
    title: "Prix sensibles",
    text: "Le budget étudiant exige des offres lisibles, rapides et vraiment accessibles.",
    icon: WalletCards,
  },
  {
    title: "Confiance et hygiène",
    text: "Les étudiants veulent des options plus propres, plus saines et disponibles aux bons horaires.",
    icon: ShieldAlert,
  },
];

export default function ProblemSection() {
  return (
    <section className="bg-white py-16">
      <div className="section-shell">
        <div className="max-w-3xl">
          <p className="text-sm font-black uppercase tracking-[0.18em] text-primary">Problème validé</p>
          <h2 className="mt-3 text-3xl font-black tracking-normal text-navy sm:text-4xl">
            La pause devient une course contre la montre.
          </h2>
          <p className="mt-4 text-lg leading-8 text-slate-600">
            L'enquête terrain montre un vrai blocage quotidien: attente, stress, manque d'options pratiques et impact
            direct sur la qualité des repas.
          </p>
        </div>

        <div className="mt-9 grid gap-4 md:grid-cols-2 lg:grid-cols-4">
          {problems.map((problem, index) => {
            const Icon = problem.icon;
            return (
              <motion.div
                key={problem.title}
                initial={{ opacity: 0, y: 16 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.05 }}
                className="rounded-lg border border-slate-200 bg-slate-50 p-5"
              >
                <div className="mb-4 flex h-11 w-11 items-center justify-center rounded-lg bg-white text-primary shadow-sm">
                  <Icon size={22} />
                </div>
                <h3 className="text-lg font-black text-navy">{problem.title}</h3>
                <p className="mt-3 text-sm leading-6 text-slate-600">{problem.text}</p>
              </motion.div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
