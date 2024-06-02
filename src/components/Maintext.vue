<template>
  <div>
    <div
      v-if="lang === 'fr' && selected == 'about'"
    >
      Je suis médecin spécialiste en médecine interne et en gériatrie qui exerce à l'Hôpital Pierre-Boucher à Longueuil et à l'Hôpital de Sainte-Anne-des-Monts en Haute-Gaspésie.
      <br/><br/>
      Je suis membre du Comité scientifique d'évaluation des médicaments à <slink link="https://inesss.qc.ca">l'INESSS</slink>
      <!--<br/><br/>
      Durant la pandémie actuelle, j'ai appris à programmer des applications Web, notamment avec <slink link="https://vuejs.org">Vue.js</slink> mes projets sont dans la section dédiée à cette fin sur cette page Web.
      -->
    </div>
    <div
      v-if="selected == 'forms'"
      class="flex-cntt "
    >
      <div v-if="lang === 'fr'" class="">
        Certains services ne sont pas couverts par la RAMQ, dont certains formulaires. Le coût et les modalités pour ces services non assurés se trouvent ci-dessous.
      </div>
      <div v-if="lang === 'fr'" class="text-weight-bold q-mt-md">
        Généralités
      </div>
      <div v-if="lang === 'fr'" class=" q-mb-sm">
        <q-list dense >
          <q-item dense class="flex-rnss">
            <div class="q-mr-sm">·</div>
            <div>le formulaire à remplir doit être apporté au rendez-vous en format papier ou PDF via courriel; il sera retourné dans le format correspondant.</div>
          </q-item>
          <q-item dense class="flex-rnss">
            <div class="q-mr-sm">·</div>
            <div>toutes les sections qui ne contiennent d'informations médicales doivent avoir été remplies, notamment les champs d'identification.</div>
          </q-item>
          <q-item dense class="flex-rnss">
            <div class="q-mr-sm">·</div>
            <div>le médecin se réserve le droit de refuser de remplir le formulaire s'il ne dispose pas de l'information requise ou si un autre médecin est mieux habileté à remplir le formulaire, notamment le médecin de famille.</div>
          </q-item>
          <q-item dense class="flex-rnss">
            <div class="q-mr-sm">·</div>
            <div>le délai à prévoir pour la rédaction est d'environ une semaine (cinq jours ouvrables).</div>
          </q-item>
          <q-item dense class="flex-rnss">
            <div class="q-mr-sm">·</div>
            <div>le paiement se fait </div>
          </q-item>
          <q-item dense>
            · le délai à prévoir pour la rédaction est d'environ une semaine (cinq jours ouvrables).
          </q-item>
        </q-list>
      </div>
      <div v-if="lang === 'fr'" class="text-weight-bold q-mt-md">
        Modalités de paiement
      </div>
      <div v-if="lang === 'fr'" class=" q-mb-sm">
        <q-list dense>
          <q-item dense class="flex-rnss">
            <div class="q-mr-sm ">· </div>
            <div><u>paiement électronique:</u> fournir une adresse courriel; un lien pour le paiement par carte de débit ou crédit vous sera envoyé, puis lorsque le paiement sera acquitté, le formulaire sera envoyé encrypté via courriel et signé numériquement. Dans ce cas, le mot de passe est le numéro d'assurance maladie à 12 chiffres, sans espace.</div>
          </q-item>
          <q-item dense class="flex-rnss">
            <div class="q-mr-sm ">· </div>
            <div><u>paiement comptant à l'Hôpital Pierre-Boucher:</u> remettre le paiement à l'agent.e administratif.ve à l'UEGM qui vous remettra un reçu et le formulaire rempli; l'adresse est <b>1205 chemin du Tremblay, Longueuil, Québec, J4N 1R4</b>, au rez-de-chaussée</div>
          </q-item>
          <q-item dense class="flex-rnss">
            <div class="q-mr-sm ">· </div>
            <div><u>paiement comptant à l'Hôpital de Sainte-Anne-des-Monts:</u> remettre le paiement à l'agent.e administratif.ve au Bureau de médecine familiale (BMF) qui vous remettra un reçu et le formulaire rempli; l'adresse est <b>50, avenue Belvédère, Sainte-Anne-des-Monts, Québec, G4V 1X4</b>, le BMF se trouve au rez-de-chaussée à l'extrême ouest du bâtiment</div>
          </q-item>
        </q-list>
      </div>
      <div v-if="lang === 'fr'" class="text-weight-bold q-mb-sm q-mt-md">
        Tarification
      </div>
      <q-list bordered class="rounded-borders fontroboto">
        <q-expansion-item class="fontroboto"
          v-for="sortedFormType in Object.keys(sortedForms)"
          :key="sortedFormType"
          expand-separator
          :icon="`mdi-${sortedFormType}`"
          :label="`${sortedFormType === 'scale-balance' ? '' : (lang === 'fr' ? 'Formulaires —' : 'Forms —')} ${catNames[sortedFormType][1 - Number(lang === 'fr')]}`"
        >
          <q-card class="q-pl-md">
            <div
              v-for="(form, formIndex) in sortedForms[sortedFormType]"
              :key="form.label"
            >
              <q-separator v-if="formIndex !== 0" spaced inset />
              <q-item class=" flex-rnbt" >
                <div class="flex-cntt">
                  <q-item-label style="font-size:12pt;" class="text-weight-medium">{{form.form}}</q-item-label>
                  <q-item-label style="font-size:11pt;" class="q-ml-md">{{form.org}}</q-item-label>
                  <q-item-label style="font-size:11pt;" caption lines="2" class="q-ml-md" v-if="form.pages !== '0'">{{`${form.label} (${form.pages} page${form.pages > 1 ? 's' : ''})`}}</q-item-label>
                  <q-item-label style="font-size:11pt;" caption lines="2" class="q-ml-md" v-if="form.pages === '0'">{{form.label}}</q-item-label>
                </div>

                <div class="flex-cnbe " style="">
                  <div class="text-weight-bold text-black" style="font-size:0.8em;white-space:nowrap;" >{{form.cost}} $</div>
                  <div class="flex-rnee " >
                    <q-icon  :name="`mdi-${form.icon}`" color="green" />
                  </div>
                </div>
              </q-item>
            </div>
          </q-card>
        </q-expansion-item>
      </q-list>
    </div>
    <div
      v-if="lang === 'fr' && selected == 'rv'" class="flex-cntt"
    >
      <div class="q-mt-md q-mb-sm">Les coordonnées pertinentes se trouvent ci-dessous, selon la nature de la consultation.</div>
      <div class="q-mt-md q-mb-sm">En tout temps, si votre état de santé requiert des soins urgents, téléphonez au <b>911</b> ou rendez-vous dans une salle d'urgence, selon ce qui est approprié.</div>
      <!--<div class="q-mt-md q-mb-sm">Si votre appel concerne un problème médical, vous aurez l'opportunité de laisser un message; un retour d'appel est à prévoir dans les cinq jours ouvrables, sauf en cas de vacances. Si ceci est trop long, vous devez consulter un autre médecin. Seuls les problèmes de santé en lien avec la raison pour laquelle le médecin vous suit feront l'objet d'un retour d'appel. Aucun appel ne sera retourné si le médecin ne vous a jamais vu.</div>-->
      <div class="q-mt-md q-mb-sm">Les appels concernant des problèmes médicaux seront retournés en cinq jours ouvrables (sauf si vacances), <u>seulement si l'appel est en lien avec ce pourquoi le médecin vous suit déjà</u>. Si ce délai est trop long, consultez un autre médecin.</div>
      <div v-if="lang === 'fr'" class="text-weight-bold q-mt-md q-mb-sm">
        Numéros généraux
      </div>
      <div v-if="lang === 'fr'" class=" q-mb-sm">
        <q-list dense class="fontroboto">
          <q-item dense class="flex-rnbs">
            <div class="q-mr-sm " :style="`width:${100-ratioLR}%;`">Téléphone</div>
            <div :style="`font-family:monospace;font-size:1em;width:${ratioLR}%;text-align:right;`"> (888) 614-1911 </div>
          </q-item>
          <q-item dense class="flex-rnbs">
            <div class="q-mr-sm " :style="`width:${100-ratioLR}%;`">Télécopieur</div>
            <div :style="`font-family:monospace;font-size:1em;width:${ratioLR}%;text-align:right;`"> (418) 763-9477</div>
          </q-item>
        </q-list>
      </div>
      <q-list padding bordered class="rounded-borders ">
        <q-expansion-item
          expand-separator
          label="Clinique de gériatrie · Hôpital Pierre-Boucher (UEGM)"
          header-class="text-weight-bold"
        >
          <q-card>
            <div v-if="lang === 'fr'" class=" q-mb-sm q-ml-md">
              <q-list dense class="fontroboto">
                <q-item dense class="flex-rnbs">
                  <div class="q-mr-sm " :style="`width:${100-ratioLR}%;`">Rendez-vous</div>
                  <div :style="`font-family:monospace;font-size:1em;width:${ratioLR}%;text-align:right;`"> (450) 396-2016</div>
                </q-item>
                <q-item dense class="flex-rnbs">
                  <div class="q-mr-sm " :style="`width:${100-ratioLR}%;`">Télécopieur</div>
                  <div :style="`font-family:monospace;font-size:1em;width:${ratioLR}%;text-align:right;`"> (450) 616-8515</div>
                </q-item>
                <q-item dense class="flex-rnbs">
                  <div class="q-mr-sm " :style="`width:${100-ratioLR}%;`">Se rendre</div>
                  <div :style="`width:${ratioLR}%;`">1205 chemin du Tremblay, Longueuil, Québec, J4N 1R4, au rez-de-chaussée</div>
                </q-item>
                <q-item dense class="flex-rnbs">
                  <div class="q-mr-sm " :style="`width:${100-ratioLR}%;`">Problème médical lié</div>
                  <div :style="`width:${ratioLR}%;`"> consultez ou laissez un message à l'infirmier.ère de la clinique de gériatrie (même numéro que pour rendez-vous)</div>
                </q-item>
                <q-item dense class="flex-rnbs">
                  <div class="q-mr-sm " :style="`width:${100-ratioLR}%;`">Demande de consultation</div>
                  <div :style="`width:${ratioLR}%;`">votre médecin doit télécopier la demande au numéro ci-dessus</div>
                </q-item>
              </q-list>
            </div>
          </q-card>
        </q-expansion-item>

        <q-expansion-item
          expand-separator
          label="Clinique de gériatrie · Hôpital de Sainte-Anne-des-Monts"
          header-class="text-weight-bold"
        >
          <q-card>
            <div v-if="lang === 'fr'" class=" q-mb-sm q-ml-md">
              <q-list dense class="fontroboto">
                <q-item dense class="flex-rnbs">
                  <div class="q-mr-sm " :style="`width:${100-ratioLR}%;`">Rendez-vous</div>
                  <div :style="`font-family:monospace;font-size:1em;width:${ratioLR}%;text-align:right;`"> (418) 763-2261 # 2780</div>
                </q-item>
                <q-item dense class="flex-rnbs">
                  <div class="q-mr-sm " :style="`width:${100-ratioLR}%;`">Télécopieur</div>
                  <div :style="`font-family:monospace;font-size:1em;width:${ratioLR}%;text-align:right;`"> (418) 763-3578</div>
                </q-item>
                <q-item dense class="flex-rnbs">
                  <div class="q-mr-sm " :style="`width:${100-ratioLR}%;`">Se rendre</div>
                  <div :style="`width:${ratioLR}%;`">50, avenue Belvédère, Sainte-Anne-des-Monts, Québec, G4V 1X4 → au rez-de-chaussée, à l'extrémité ouest du bâtiment</div>
                </q-item>
                <q-item dense class="flex-rnbs">
                  <div class="q-mr-sm " :style="`width:${100-ratioLR}%;`">Problème médical lié</div>
                  <div :style="`width:${ratioLR}%;`"> consultez ou laissez un message à l'infirmier.ère de la clinique de gériatrie (même numéro que pour rendez-vous)</div>
                </q-item>
                <q-item dense class="flex-rnbs">
                  <div class="q-mr-sm " :style="`width:${100-ratioLR}%;`">Demande de consultation</div>
                  <div :style="`width:${ratioLR}%;`">votre médecin doit télécopier la demande au numéro ci-dessus ou la transmettre à rendez-vous.cisssgaspesie@ssss.gouv.qc.ca</div>
                </q-item>
              </q-list>
            </div>
          </q-card>
        </q-expansion-item>

        <q-expansion-item
          expand-separator
          label="Clinique de médecine interne · Hôpital de Sainte-Anne-des-Monts"
          header-class="text-weight-bold"
        >
          <q-card>
            <div v-if="lang === 'fr'" class=" q-mb-sm  q-ml-md">
              <q-list dense class="fontroboto">
                <q-item dense class="flex-rnbs">
                  <div class="q-mr-sm " :style="`width:${100-ratioLR}%;`">Rendez-vous</div>
                  <div :style="`font-family:monospace;font-size:1em;width:${ratioLR}%;text-align:right;`"> (418) 763-2261 # 2070</div>
                </q-item>
                <q-item dense class="flex-rnbs">
                  <div class="q-mr-sm " :style="`width:${100-ratioLR}%;`">Télécopieur</div>
                  <div :style="`font-family:monospace;font-size:1em;width:${ratioLR}%;text-align:right;`"> (418) 763-9477</div>
                </q-item>
                <q-item dense class="flex-rnbs">
                  <div class="q-mr-sm " :style="`width:${100-ratioLR}%;`">Problème médical lié</div>
                  <div :style="`font-family:monospace;font-size:1em;width:${ratioLR}%;text-align:right;`"> (418) 763-2261 # 2120</div>
                </q-item>
                <q-item dense class="flex-rnbs">
                  <div class="q-mr-sm " :style="`width:${100-ratioLR}%;`">Se rendre</div>
                  <div :style="`width:${ratioLR}%;`">50, avenue Belvédère, Sainte-Anne-des-Monts, Québec, G4V 1X4 → se rendre au premier étage</div>
                </q-item>
                <q-item dense class="flex-rnbs">
                  <div class="q-mr-sm " :style="`width:${100-ratioLR}%;`">Demande de consultation</div>
                  <div :style="`width:${ratioLR}%;`">votre médecin doit télécopier la demande au numéro ci-dessus ou la transmettre à rendez-vous.cisssgaspesie@ssss.gouv.qc.ca</div>
                </q-item>
              </q-list>
            </div>
          </q-card>
        </q-expansion-item>
      </q-list>
      <!--Pour prendre rendez-vous à l'<slink>Hôpital de Sainte-Anne-des-Monts</slink>, contactez le centre de rendez-vous.
      <sicon :dat="[['email', 'rendez-vous.cisssgaspesie'], ['', '@ssss.gouv.qc.ca'], ['call', '+1 418 763-2261 # 2070']]" />
      <br/><br/>
      Pour prendre rendez-vous à l'<slink>Hôpital Pierre-Boucher</slink>, contactez l'UEGM.
      <sicon :dat="[['call', '+1 450 396-2016'], ['fax', '+1 450 616-8515']]" />
      <br/><br/>-->
    </div>
    <div
      v-if="lang === 'fr' && selected == 'mds'"
    >
      Pour me joindre, vous pouvez m'adresser un courriel à l'adresse <span style="font-family:monospace;">@ssss.gouv.qc.ca</span> que vous pouvez retrouver sur le répertoire Outlook.
      <br/><br/>
      Le numéro général pour me joindre pour les professionnels de la santé est le <b>(888) 614-1911, option 3</b>.
      <br/><br/>
      Autrement, les coordonnées pertinentes sont inscrites ci-dessous.
      <div v-if="lang === 'fr'" class="text-weight-bold q-mt-md q-mb-sm">
        Coordonnées
      </div>
      <div v-if="lang === 'fr'" class=" q-mb-sm">
        <q-list dense class="fontroboto">
          <q-item dense class="flex-rnbs">
            <div class="q-mr-sm " ><u>Hôpital Pierre-Boucher</u></div>
          </q-item>
          <q-item dense class="flex-rnbs q-ml-md">
            <div class="q-mr-sm " style="width:50%;">Téléphone (patients admis)</div>
            <div style="font-family:monospace;font-size:1em;width:50%;text-align:right;"> (450) 468-8111 # 0 </div>
          </q-item>
          <q-item dense class="flex-rnbs q-ml-md">
            <div class="q-mr-sm " style="width:50%;">Téléphone (patients externes)</div>
            <div style="font-family:monospace;font-size:1em;width:50%;text-align:right;"> (450) 396-2016 </div>
          </q-item>
          <q-item dense class="flex-rnbs q-ml-md">
            <div class="q-mr-sm " style="width:50%;">Télécopieur</div>
            <div style="font-family:monospace;font-size:1em;width:50%;text-align:right;"> (418) 763-9477</div>
          </q-item>
          <q-item dense class="flex-rnbs q-ml-md">
            <div class="q-mr-sm " style="width:50%;">Demandes de consultation</div>
            <div style="font-family:monospace;font-size:1em;width:50%;text-align:right;"> par télécopieur ↑</div>
          </q-item>
          <q-item dense class="flex-rnbs">
            <div class="q-mr-sm q-mt-md" ><u>Hôpital de Sainte-Anne-des-Monts</u></div>
          </q-item>
          <q-item dense class="flex-rnbs q-ml-md">
            <div class="q-mr-sm " style="width:50%;">Téléphone</div>
            <div style="font-family:monospace;font-size:1em;width:50%;text-align:right;"> (418) 763-2261 # 0 </div>
          </q-item>
          <q-item dense class="flex-rnbs q-ml-md">
            <div class="q-mr-sm " style="width:50%;">Télécopieur général</div>
            <div style="font-family:monospace;font-size:1em;width:50%;text-align:right;"> (418) 763-9477</div>
          </q-item>
          <q-item dense class="flex-rnbs q-ml-md">
            <div class="q-mr-sm " style="width:50%;">Demandes de consultation</div>
            <div style="font-family:monospace;font-size:1em;width:50%;text-align:right;"> par télécopieur ↑</div>
          </q-item>
          <q-item dense class="flex-rnbs q-ml-lg" style="top:-6pt;">
            <div class="q-mr-sm q-ml-sm " style="width:50%;">(médecine interne)</div>
            <div style="font-family:monospace;font-size:1em;width:50%;text-align:right;white-space:normal;"> ou par <a href="mailto:rendez-vous.cisssgaspesie@ssss.gouv.qc.ca">courriel</a> </div>
          </q-item>
          <q-item dense class="flex-rnbs q-ml-md ">
            <div class="q-mr-sm " style="width:50%;">Télécopieur · clinique de gériatrie</div>
            <div style="font-family:monospace;font-size:1em;width:50%;text-align:right;"> (418) 763-3578</div>
          </q-item>
          <q-item dense class="flex-rnbs q-ml-md">
            <div class="q-mr-sm " style="width:50%;">Demandes de consultation</div>
            <div style="font-family:monospace;font-size:1em;width:50%;text-align:right;"> par télécopieur ↑</div>
          </q-item>
          <q-item dense class="flex-rnbs q-ml-lg" style="top:-6pt;">
            <div class="q-mr-sm q-ml-sm " style="width:50%;">(gériatrie)</div>
            <div style="font-family:monospace;font-size:1em;width:50%;text-align:right;white-space:normal;"> ou par <a href="mailto:rendez-vous.cisssgaspesie@ssss.gouv.qc.ca">courriel</a> </div>
          </q-item>
        </q-list>
      </div>
    </div>
    <div
      v-if="lang === 'fr' && selected == 'contact'"
    >
      Allez dans la section appropriée selon que vous soyez un patient ou un professionnel.
    </div>
    <div
      v-if="lang === 'en' && selected == 'about'"
    >
      I am an internist and geriatrician working at Hôpital Pierre-Boucher in Longueuil and Hôpital de Sainte-Anne-des-Monts in La Haute-Gaspésie.
      <br/><br/>
      I sit on <slink link="https://inesss.qc.ca">INESSS'</slink> Comité scientifique d'évaluation des médicaments à des fins d'inscription.
      <!--<br/><br/>
      Durant la pandémie actuelle, j'ai appris à programmer des applications Web, notamment avec <slink link="https://vuejs.org">Vue.js</slink> mes projets sont dans la section dédiée à cette fin sur cette page Web.
      -->
    </div>
    <div
      v-if="lang === 'en' && selected == 'rv'"
    >
      For an appointment at <slink>Hôpital de Sainte-Anne-des-Monts</slink>, contact the appointment center.
      <sicon :dat="[['email', 'rendez-vous.cisssgaspesie@ssss.gouv.qc.ca'], ['call', '+1 418 763-2261 # 2070']]" />
      <br/><br/>
      For an appointment at <slink>Hôpital Pierre-Boucher</slink>, contact the UEGM.
      <sicon :dat="[['call', '+1 450 396-2016'], ['fax', '+1 450 616-8515']]" />
      <br/><br/>
    </div>
    <div
      v-if="lang === 'en' && selected == 'mds'"
    >
      To contact me, you can use my standard <span style="font-family:monospace;">@ssss.gouv.qc.ca</span> email address which can be found on the Outlook directory. Otherwise, the relevant phone numbers are written below.
      <br/><br/>
      Hôpital de Sainte-Anne-des-Monts
      <sicon :dat="[['call', '+1 418 763-2261 # 0']]" />
      <br/>
      Hôpital Pierre-Boucher
      <sicon :dat="[['call', '+1 450 468 8111 # 0']]" />
      <br/><br/>
    </div>
    <div
      v-if="lang === 'en' && selected == 'contact'"
    >
      Visit the appropriate section depending on if you are a patient or a healthcare worker.
    </div>
  </div>
</template>
<script>
import { defineComponent } from 'vue'
import Slink from "../components/Slink.vue"
import Sicon from "../components/Sicon.vue"

export default defineComponent({
  name: 'Maintext',
  components: { Slink, Sicon },
  props: {
    lang: { type: String, required: false, default() { return 'fr' } },
    selected: { type: String, required: false, default() { return 'about' } },
    sections: { type: Object, required: false, default() { return {} } },
    forms: { type: Array, required: false, default() { return [] } }
  },
  data() {
    return {
      ratioLR: 70,
      catNames: {
        'train-car': ['transport', 'transport'],
        'scale-balance': ['Légal', 'Legal'],
        'medical-bag': ['attestation médicale', 'medical certificate'],
        'pill': ['ordonnances', 'prescriptions'],
        'human-wheelchair': ['personnes avec handicap', 'individuals with a handicap'],
        'bank-outline': ['crédits d\'impôts autres', 'other tax credits'],
        'handshake-outline': ['perte d\'autonomie', 'loss of autonomy'],
        'ambulance': ['fin de vie', 'end of life']
      }
    }
  },
  computed: {
    sortedFormsLABEL () {
      const sortedLabels = JSON.parse(JSON.stringify(this.forms)).reduce((a, x) => a.includes(x.label) ? a : [a, [x.label]].flat(), [])
      return sortedLabels.map(x => this.forms.filter(y => y.label === x)[0])
    },
    sortedForms () {
      const sortedLabels = JSON.parse(JSON.stringify(this.forms)).reduce((a, x) => a.includes(x.icon) ? a : [a, [x.icon]].flat(), [])
      // return sortedLabels.map(x => this.forms.filter(y => y.icon === x)).flat()
      return sortedLabels.reduce((d, x) => { return { ...d, [x]: this.forms.filter(y => y.icon === x) } }, {})
    }
  },
  methods: {
    goTo (where) {
      window.open(where)
    }
  }
})
</script>
