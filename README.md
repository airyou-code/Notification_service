<h1 align="center">Notification Service</h1>

---

<p align="center">
Redesigned and Wrapped for Vue.js by [Divyansh Tripathi](https://silentlad.com)



<p align="center">
<img src="https://media.giphy.com/media/VFvkCMvXvlTNAGuaZm/giphy.gif">
</p>

# Installation

`npm i --save vue2-baremetrics-calendar`

## Usage

### Global Usage

Global Registeration via Vue.use() method.

```js
// main.js
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
// import the plugin
import Calendar from "vue2-baremetrics-calendar";

Vue.config.productionTip = false;

// use the plugin
Vue.use(Calendar);

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
```

Once registered you can use the component in its default settings with as follows:-

```html
<Calendar
  type="double"
  @rangeEdit="processDateRange()"
  elementName="doubleRangePicker"
/>

<Calendar
  type="single"
  @dateEdit="processDate()"
  elementName="singleRangePicker"
/>
```

**REMEMBER _elementName_ is the only required prop and it should be different for each datepicker in your component**

```html
<template>
  <div id="app">
    <Calendar
      @rangeEdit="processOutput"
      type="double"
      elementName="otherRangePicker"
    />

    <Calendar
      @dateEdit="processOutput"
      type="single"
      elementName="primaryRangePicker"
    />
  </div>
</template>

<script>
  import Calendar from "./components/Calendar";
  export default {
    components: {
      Calendar
    },
    methods: {
      processOutput(output) {
        console.log(output);
      }
    }
  };
</script>