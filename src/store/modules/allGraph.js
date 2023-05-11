const state = {
    graphData: []
}
  
const mutations = {
    SET_ALL_GRAPH: (state, newval) => {
        state.logs.push(newval)
    },
}

export default {
    namespaced: true,
    state,
    mutations,
  }