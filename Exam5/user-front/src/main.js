// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.config.productionTip = false

Vue.use(Element);
/* eslint-disable no-new */

Vue.prototype.dateToString = function (date) {
  let y = date.getFullYear();
  let m = date.getMonth() + 1;
  m = m < 10 ? ('0' + m) : m;
  let d = date.getDate();
  d = d < 10 ? ('0' + d) : d;
  let h = date.getHours();
  h = h < 10 ? ('0' + h) : h;
  let minute = date.getMinutes();
  let second = date.getSeconds();
  minute = minute < 10 ? ('0' + minute) : minute;
  second = second < 10 ? ('0' + second) : second;
  return y + '-' + m + '-' + d + ' ' + h + ':' + minute + ':' + second;
};
Vue.prototype.timestampToString = function (timeStamp) {
  let date = new Date(timeStamp);
  return this.dateToString(date);
};
Vue.prototype.formatObjectData = function (data) {
  Object.keys(data).forEach(k => {
    if (data[k] == undefined) {
      data[k] = "";
    }
    if (k == "ctime" || k == "startTime" || k == "endTime") {
      data[k] = this.timestampToString(data[k]);
    } else {
      data[k] = String(data[k]);
    }
  });
};

Vue.prototype.setCookie = function (name, value, exDays) {
  let d = new Date();
  d.setTime(d.getTime() + (exDays * 24 * 60 * 60 * 1000));
  let expires = "expires=" + d.toUTCString();
  document.cookie = name + "=" + value + "; " + expires;
};
Vue.prototype.clearCookie = function (name) {
  this.setCookie(name, "", -1);
};
Vue.prototype.getCookie = function (cname) {
  let name = cname + "=";
  let ca = document.cookie.split(';');
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') c = c.substring(1);
    if (c.indexOf(name) != -1) return c.substring(name.length, c.length);
  }
  return "";
};

new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
