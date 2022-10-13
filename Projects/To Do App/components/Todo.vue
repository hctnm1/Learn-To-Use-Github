<template>
  <div :class="`task ${task.done ? 'is-complete' : ''}`">
      <div class="content">{{ task.content }}</div>
      <div class="buttons">
          <button @click="statusTask" class="status"> {{ task.done ? 'Completed' : 'Ongoing' }}</button>
          <button @click="clearTask" class="clear">Clear</button>
      </div>
  </div>
</template>

<script>
export default {
    props: ['task'],
    methods: {
        statusTask(task) {
            this.$store.commit('status', this.task);
        },
        clearTask(task) {
            this.$store.commit('clear', this.task);
        }
    }
}
</script>
