<template>
  <div class="hello">
    <p>{{ state.msg }}</p>
    <button @click="onClick">
      {{ text }}
    </button>
  </div>
</template>

<script>
import { reactive } from "vue";

export default {
  props: {
    text: {
      type: String,
      required: true
    },
    msg: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const state = reactive({
      msg: props.msg,
    });

    const decoder = new TextDecoder("utf-8");

    console.log(props.msg);

    function onClick() {
      const url = "http://localhost:9000"
      fetch(url).then((data) => {
        const reader = data.body.getReader();
        reader.read().then(({ value }) => {
          state.msg = decoder.decode(value);
        });
      });
    }

    return {
      state,
      onClick
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  button {
    background-color: aquamarine;
  }
</style>
