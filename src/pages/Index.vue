<template>
  <q-layout view="hHh lpR fFf">
    <!--<q-header
      style="height:60px;"
    >
      a
    </q-header>
    <q-drawer show-if-above v-model="drawer" side="left" bordered>
    </q-drawer>-->
    <q-page style="height:100%;">
      <div class="flex-cnsc " style="height:100vh;" >
        <q-resize-observer @resize="size = $event" />
        <div
          v-if="!mobile"
          style="flex:0.2;max-height:120px;"
          class=""
        >
        </div>
        <div
          class="flex-rnbs"
          :style="`width:100%;max-width:${mobile ? threshold : widths[0]}px;flex:1;`"
        >
          <ltmenu
            v-if="!mobile"
            :selected="selected"
            :sections="sections"
            :lang="lang"
            :mobile="mobile"
            @select="selected = $event"
          />
          <div
            class="flex-rnss "
            style="width:75%;min-width:50%;flex-grow:1;height:100%;"
          >
            <div
              :style="`width:100%;max-width:${mobile ? threshold : widths[1]}px;height:100%;`"
              class="flex-cnbt "
            >
              <div
                class="flex-cnss"
              >
                <div class="flex-rnbc" style="width:100%;">
                  <div
                    :class="`flex-rnbc ${mobile ? 'q-ma-sm' : ''}`"
                    style="font-family: 'Krona One', sans-serif;"
                  >
                    <img
                      class="q-mr-md"
                      v-if="mobile"
                      style="height:40px;width:40px;"
                      src="../assets/icon1.png"
                    />
                    <div>ALEX HALME</div>
                  </div>
                  <div class="font-left text-weight-normal flex-rwee q-ma-sm" style="font-size:12pt;align-self:start;min-width:60px;">
                    <div
                      @click="lang = 'fr'"
                      :style="`${lang === 'fr' ? 'opacity:1;text-decoration: underline;' : 'opacity:1;cursor:pointer;'}`"
                    >
                      FR
                    </div>
                    <div class="q-mx-xs">/</div>
                    <div
                      @click="lang = 'en'"
                      :style="`${lang === 'en' ? 'opacity:1;text-decoration: underline;' : 'opacity:1;cursor:pointer;'}`"
                    >
                      EN
                    </div>
                  </div>
                </div>
                <div
                  :style="`margin-top:${margintop[mobile]}px;font-family: 'PT Serif', serif;font-size:1.2em;width:100%;`"
                  class="flex-cntt"
                >
                  <ltmenu
                    v-if="mobile"
                    :selected="selected"
                    :sections="sections"
                    :lang="lang"
                    :mobile="mobile"
                    @select="selected = $event"
                  />
                  <maintext :class="mobile ? 'q-pa-sm' : ''" style="width:100%;"
                    :lang="lang"
                    :selected="selected"
                    :sections="sections"
                    :forms="forms"
                  />
                </div>
              </div>
              <div
                :class="`flex-rnbc q-mb-sm ${mobile ? 'q-px-sm' : ''}`"
              >
                <div
                  class="left-font text-weight-medium"
                  style="font-size:1.2em;opacity:0.6;"
                >
                  <span style="display:inline-block; transform: rotate(180deg);">&copy;</span> 2022 Alex Halme
                </div>
                <div>
                  <img
                    v-for="(svgdat, svgdatIndex) in svgs"
                    :key="`svg-${svgdatIndex}`"
                    class="icon-opacity q-mr-sm"
                    :style="`height: ${svgdat[2]}px;width: ${svgdat[2]}px;`"
                    :src="svgdat[0]"
                    @click="goTo(svgdat[1])"
                  />
                  <!--text-gray-400 dark:text-gray-500 hover:opacity-80-->
                </div>
              </div>
            </div>
            <div
              :style="`margin-top:${margintop[mobile]}px;font-family: 'PT Serif', serif;font-size:1.5em;`"
            >
            </div>
          </div>
        </div>
      </div>
    </q-page>
  </q-layout>
</template>

<script>
import Maintext from 'src/components/Maintext.vue'
import { defineComponent } from "vue"
import Ltmenu from "../components/Ltmenu.vue"
import $ from 'jquery'

// https://mitchellh.com/
export default defineComponent({
  components: { Maintext, Ltmenu },
  name: "PageIndex",
  data () {
    return {
      threshold: 650,
      size: { width: 0 },
      widths: [1050, 550],
      margintop: { true: -30, false: 80 },
      lang: 'fr',
      selected: 'about',
      sections: {
        about: { fr: 'À propos', en: 'About' },
        rv: { fr: 'Rendez-vous', en: 'Appointments' },
        forms: { fr: 'Formulaires', en: 'Forms' },
        mds: { fr: 'Professionnels', en: 'Healthcare workers' },
        contact: { fr: 'Contact', en: 'Contact' }
        // projects: { fr: 'Projets', en: 'Projects' }
      },
      svgs: [
        ['cmq8', 'http://cmq.org/bottin/details.aspx?id=36B6BFFFBB1CD73A0499C1AA1E364821&lang=fr&a=1', 29],
        ['twitter', 'https://twitter.com/alex_halme?lang=en', 24],
        ['github', 'https://github.com/alexhalme', 24]
      ].map(x => [require(`../assets/${x[0]}.svg`), x[1], x[2]]),
      drawer: true,
      forms: [],
      server: null
    }
  },
  computed: {
    mobile () {
      return this.size.width < this.threshold
    }
  },
  mounted () {
    this.selected = Object.keys(this.sections)[0]
    this.server = 'https://alexhal.me/'
    if (/^.*(localhost|127.0.0.1):.*$/.test(window.location.href)) {
      this.server = 'http://127.0.0.1:5145/'
      if (!/^.*(localhost|127.0.0.1):5145.*$/.test(window.location.href)) {
        window.location.href = 'http://127.0.0.1:5145'
      }
    }
    if (!/^.*(localhost:5145|127.0.0.1:5145|alexhal.me).*$/.test(window.location.href)) {
      return false
    }
    $.ajax({
      url: `${this.server}fees`,
      type: 'get',
      success: ((retval) => {
        this.forms = retval
      }),
      error: ((error) => {
        console.log(error)
      })
    })
  },
  methods: {
    goTo (where) {
      window.open(where)
    }

  }
})
</script>
<style scoped>
  .left-font {
    font-family: Inter,ui-sans-serif,system-ui,-apple-system;
  }
  .icon-opacity {
    opacity: 0.4;
    filter: grayscale(100%);
    cursor:pointer;
  }
  .icon-opacity:hover {
    opacity: 0.2;
  }
</style>
