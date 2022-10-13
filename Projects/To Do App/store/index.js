export const state = () => ({
  value: []
})

export const mutations = {
  new(state, task) {
      state.value = [{ content: task, done: false }, ...state.value];
  },

  clear(state, task) {
      state.value.splice(state.value.indexOf(task), 1);
  },

  status(state, task) {
      task.done = !task.done;
  }
}
