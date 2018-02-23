import Vue from 'vue';
import App from './App';
import router from './router';
import axios from 'axios';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-default/index.css';    // 默认主题
// import '../static/css/theme-green/index.css';       // 浅绿色主题
import "babel-polyfill";

Vue.use(ElementUI);
Vue.prototype.$axios = axios;
new Vue({
    router,
    render: h => h(App)
}).$mount('#app');

Vue.prototype.timestampToString = function(timeStamp) {
    let date = new Date(timeStamp);
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
    return y + '-' + m + '-' + d+' '+h+':'+minute+':'+second;
};
Vue.prototype.formmatObjectData = function(data) {
    Object.keys(data).forEach(k => {
        if (data[k] == undefined){
            data[k] = "";
        }
        if (k == "ctime" || k == "startTime" || k == "endTime") {
            data[k] = this.timestampToString(data[k]);
        } else{
            data[k] =  String(data[k]);
        }
    });
}
