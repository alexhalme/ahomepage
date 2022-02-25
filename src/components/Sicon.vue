<template>
  <div class="flex-cntt q-mt-sm">
    <div
      v-for="datum in dat"
      :key="JSON.stringify(datum)"
      class="flex-rnsc q-ml-lg q-mb-xs"
    >
      <q-icon
        :name="datum[0]"
      />
      <div
        class="q-ml-md"
        style="font-family:monospace;font-size:1em;"
      >
        {{datum[1]}}
      </div>
    </div>
  </div>
</template>
<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'Sicon',
  props: {
    dat: { type: Array, required: false, default() { return [] } }
  },
  methods: {
    goTo () {
      window.open(this.link)
    }
  }
})
</script>
