<template>
  <div>
    poulet
  </div>
</template>
<script>

export default defineComponent({
  name: 'items',
  props: {
  },
  methods: {
    goTo () {
      window.open(this.link)
    }
  }
})
</script>
