import { motion } from "framer-motion";
import { Check, Clock, CreditCard, PackageCheck } from "lucide-react";

const steps = [
  { title: "Choisir", text: "Filtrer par budget, healthy, sandwichs, tacos ou boissons.", icon: Check },
  { title: "Planifier", text: "Sélectionner un pickup time adapté à la pause.", icon: Clock },
  { title: "Confirmer", text: "Voir le prix en MAD, le délai estimé et le statut.", icon: CreditCard },
  { title: "Récupérer", text: "Passer au pickup quand la commande devient Ready.", icon: PackageCheck },
];

export default function HowItWorks() {
  return (
    <section className="py-16">
      <div className="section-shell">
        <div className="flex flex-col justify-between gap-5 md:flex-row md:items-end">
          <div>
            <p className="text-sm font-black uppercase tracking-[0.18em] text-primary">How it works</p>
            <h2 className="mt-3 text-3xl font-black tracking-normal text-navy sm:text-4xl">Quatre actions simples.</h2>
          </div>
          <p className="max-w-2xl text-base leading-7 text-slate-600">
            Le parcours est volontairement court pour un usage réel entre deux cours, sur mobile, avec une décision en
            moins d'une minute.
          </p>
        </div>

        <div className="mt-9 grid gap-4 md:grid-cols-2 lg:grid-cols-4">
          {steps.map((step, index) => {
            const Icon = step.icon;
            return (
              <motion.div
                key={step.title}
                initial={{ opacity: 0, y: 16 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.06 }}
                className="card p-5"
              >
                <div className="flex items-center justify-between">
                  <span className="text-sm font-black text-slate-400">0{index + 1}</span>
                  <div className="flex h-11 w-11 items-center justify-center rounded-lg bg-navy text-white">
                    <Icon size={21} />
                  </div>
                </div>
                <h3 className="mt-5 text-xl font-black text-navy">{step.title}</h3>
                <p className="mt-3 text-sm leading-6 text-slate-600">{step.text}</p>
              </motion.div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
