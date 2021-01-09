<template>
  <div class="hello">
    <p>{{ state.msg }}</p>
    <button @click="onClick">
      echo!
    </button>
  </div>
</template>

<script>
import { reactive } from "vue";

export default {
  setup() {
    const state = reactive({
      msg: "empty",
    });

    const decoder = new TextDecoder("utf-8");

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
      onClick,
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
