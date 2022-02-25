<template>
  <div
    :class="mobile ? 'flex-rnbs' : 'flex-cnss'"
    :style="mobile ? '' : 'width:25%;min-width:150px;'"
  >
    <div
      v-if="mobile"
      class="flex-cntt"
      style="order:2;"
    >
      <div style="font-family: 'Krona One', sans-serif;">
        ALEX HALME
      </div>
      <q-breadcrumbs class=" flex-cntt"
        v-for="(bc, bcIndex) in parsedBC"
        :key="`bc-${bcIndex}`"
        gutter="md"
        style="min-width:100%;white-space:nowrap;"
      >
        <template #separator>
          <div class="text-weight-bold" :style="(bcGreen[bcIndex] || (!moveGreen)) ? 'margin-top:-6px;' : 'margin-top:4px;'">
            /
          </div>
        </template>
        <q-breadcrumbs-el
          v-for="section in bc"
          :key="section"
          class="flex-cncc "
          style="height:100%;"
        >
          <div
            @click="$emit('select', section)"
            :class="`text-weight-medium ${selected === section ? 'text-green-8': ''}`"
            :style="`height:22px;${selected !== section ? 'cursor:pointer;' : ''}font-size:1.2em;font-family: Inter,ui-sans-serif,system-ui,-apple-system;`"
          >
            {{sections[section][lang]}}
          </div>
          <div
            @click="$emit('select', section)"
            v-if="bcGreen[bcIndex] || (!moveGreen)"
            :class="`left-font text-weight-bolder ${selected === section ? 'text-green-8': ''}`"
            :style="`height:18px;width:14px;font-size:1.4em;margin-top:-7px;${selected !== section ? 'cursor:pointer;' : ''}`"
          >
            {{selected === section ? '•' : '' }}
          </div>
        </q-breadcrumbs-el>

      </q-breadcrumbs>
    </div>
    <div
      :class="mobile ? '' : 'q-ml-lg'"
    >
      <img
        class="q-mr-md"
        v-if="true"
        style="height:40px;width:40px;"
        src="../assets/icon1.png"
      />
      <img
        v-if="false"
        style="height:auto;width:90px;"
        src="../assets/icon2.png"
      />
    </div>
    <q-list dense
      v-if="!mobile"
      style="margin-top:50px;"
    >
      <q-item
        v-for="section in Object.keys(sections)"
        :key="section"
        class="flex-rnsc"
      >
        <div
          :class="`left-font text-weight-bolder ${selected === section ? 'text-green-8': ''}`"
          style="width:14px;font-size:1.4em;"
        >
          {{selected === section ? '•' : '' }}
        </div>
        <div
          @click="$emit('select', section)"
          :class="`text-weight-medium ${selected === section ? 'text-green-8': ''}`"
          :style="`${selected !== section ? 'cursor:pointer;' : ''}font-size:1.2em;font-family: Inter,ui-sans-serif,system-ui,-apple-system;`"
        >
          {{sections[section][lang]}}
        </div>
      </q-item>
    </q-list>
  </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'Ltmenu',
  props: {
    sections: { type: Object, required: false, default () { return {} } },
    lang: { type: String, required: false, default() { return 'fr' } },
    mobile: { type: Boolean, required: false, default() { return false } },
    selected: { type: String, required: false, default() { return 'about' } }
  },
  data () {
    return {
      moveGreen: false
    }
  },
  computed: {
    parsedBC () {
      const retval = []
      let acc = []
      for (const i in Object.keys(this.sections)) {
        if (acc.length === 3) {
          retval.push(acc)
          acc = []
        }
        acc.push(Object.keys(this.sections)[i])
      }
      return [retval, [acc]].flat()
    },
    bcGreen () {
      return this.parsedBC.map(xx => xx.reduce((aa, yy) => yy === this.selected ? true : aa, false))
    }
  }
})
</script>
