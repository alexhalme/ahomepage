<template>
  <span
    style="text-decoration: underline; cursor:pointer;"
    :class="link === null ? '' : 'text-green-8'"
    @click="goTo"
  >
    <slot></slot>
  </span>
</template>
<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'Slink',
  props: {
    link: { type: String, required: false, default() { return null } }
  },
  methods: {
    goTo () {
      window.open(this.link)
    }
  }
})
</script>
