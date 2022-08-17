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
      class="flex-cntt"
    >
      <div v-if="lang === 'fr'">
        Les formulaires
      </div>
      <q-list bordered class="rounded-borders">
        <!--<div
          v-for="form in sortedForms"
          :key="form.label"
        >
          <q-item class="fontroboto flex-rnbt" >
            <div class="flex-cntt">
              <q-item-label>{{`${lang === 'fr' ? 'Formulaire' : 'Form'} ${form.form}`}}</q-item-label>
              <q-item-label caption lines="2">{{form.label}}</q-item-label>
            </div>

            <div class="flex-cnbe " style="">
              <div class="text-weight-bold text-black" style="font-size:0.8em;white-space:nowrap;" >{{form.cost}} $</div>
              <div class="flex-rnee " >
                <q-icon  :name="`mdi-${form.icon}`" color="green" />
              </div>
            </div>
          </q-item>
          <q-separator spaced inset />
        </div>-->
        <q-expansion-item class="fontroboto"
          v-for="sortedFormType in Object.keys(sortedForms)"
          :key="sortedFormType"
          expand-separator
          :icon="`mdi-${sortedFormType}`"
          :label="`${lang === 'fr' ? 'Formulaires —' : 'Forms —'} ${catNames[sortedFormType][1 - Number(lang === 'fr')]}`"
        >
          <q-card class="q-pl-md">
            <div
              v-for="(form, formIndex) in sortedForms[sortedFormType]"
              :key="form.label"
            >
              <q-separator v-if="formIndex !== 0" spaced inset />
              <q-item class=" flex-rnbt" >
                <div class="flex-cntt">
                  <q-item-label>{{`${lang === 'fr' ? 'Formulaire' : 'Form'} ${form.form}`}}</q-item-label>
                  <q-item-label caption lines="2">{{`${form.label} (${form.pages} page${form.pages > 1 ? 's' : ''})`}}</q-item-label>
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
      v-if="lang === 'fr' && selected == 'rv'"
    >
      Pour prendre rendez-vous à l'<slink>Hôpital de Sainte-Anne-des-Monts</slink>, contactez le centre de rendez-vous.
      <sicon :dat="[['email', 'rendez-vous.cisssgaspesie'], ['', '@ssss.gouv.qc.ca'], ['call', '+1 418 763-2261 # 2070']]" />
      <br/><br/>
      Pour prendre rendez-vous à l'<slink>Hôpital Pierre-Boucher</slink>, contactez l'UEGM.
      <sicon :dat="[['call', '+1 450 396-2016'], ['fax', '+1 450 616-8515']]" />
      <br/><br/>
    </div>
    <div
      v-if="lang === 'fr' && selected == 'mds'"
    >
      Pour me joindre, vous pouvez m'adresser un courriel à l'adresse <span style="font-family:monospace;">@ssss.gouv.qc.ca</span> que vous pouvez retrouver sur le répertoire Outlook. Autrement, les numéros de téléphone pertinents sont inscrits ci-dessous.
      <br/><br/>
      Hôpital de Sainte-Anne-des-Monts
      <sicon :dat="[['call', '+1 418 763-2261 # 0']]" />
      <br/>
      Hôpital Pierre-Boucher
      <sicon :dat="[['call', '+1 450 468 8111 # 0']]" />
      <br/><br/>
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
      catNames: {
        'train-car': ['transport', 'transport'],
        'scale-balance': ['légal', 'legal'],
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
