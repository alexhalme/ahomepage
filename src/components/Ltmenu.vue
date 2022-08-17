<template>
  <div
    :class="mobile ? 'flex-cntt q-mb-md' : 'flex-cnss'"
    :style="mobile ? 'width:100%;' : 'width:25%;min-width:150px;'"
  >
    <div
      v-if="!mobile"
      class="q-ml-lg"
    >
      <img
        class="q-mr-md"
        v-if="true"
        style="height:40px;width:40px;"
        src="../assets/icon1.png"
      />
    </div>
    <q-list dense
      :style="`margin-top:50px;${mobile ? 'border-top: 2px solid black;border-bottom: 2px solid black;' : ''}`"
    >
      <div
        v-for="section in parsedSection"
        :key="section"
        class="flex-cntt"
      >
        <q-item dense
          class="flex-rnsc"
        >
          <div
            :class="`left-font text-weight-bolder ${selected === section ? 'text-green-8': ''}`"
            style="width:14px;font-size:1.4em;"
          >
            {{selected === section ? '•' : '' }}
          </div>
          <div
            @click="selectSection(section)"
            :class="`text-weight-medium ${selected === section ? 'text-green-8': ''}`"
            :style="`${selected !== section ? 'cursor:pointer;' : ''}font-size:1.2em;font-family: Inter,ui-sans-serif,system-ui,-apple-system;`"
          >
            {{sections[section][lang]}}
          </div>
        </q-item>
        <q-separator size="2px;" color="black" v-if="section === selected && parsedUnrolled && mobile" />
      </div>
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
    mobile: { type: Boolean, required: false, default() { return True } },
    selected: { type: String, required: false, default() { return 'about' } }
  },
  data () {
    return {
      moveGreen: false,
      unrolled: true
    }
  },
  methods: {
    selectSection (section) {
      if (section === this.selected && this.mobile) {
        this.unrolled = !this.unrolled
        return false
      }
      this.$emit('select', section)
    }
  },
  computed: {
    parsedUnrolled () {
      return !this.mobile ? true : this.unrolled
    },
    parsedSection () {
      if (!this.mobile) {
        return Object.keys(this.sections)
      }
      return [
        [this.selected],
        this.parsedUnrolled ? Object.keys(this.sections).filter(x => x !== this.selected) : []
      ].flat()
    },
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
