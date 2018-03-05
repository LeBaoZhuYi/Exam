<template>
  <div class="main">
    <!--nr start-->
    <div class="test_main">
      <div class="nr_left">
        <div class="test">
          <form action="" method="post">
            <div class="test_title">
              <p class="test_time">
                <i class="icon iconfont">&#xe6fb;</i><b class="alt-1">01:40</b>
              </p>
              <!--<input type="button" name="test_jiaojuan" value="交卷">-->
              <el-button type="success" @click="postAnswer()">交卷</el-button>
            </div>

            <div class="test_content">
              <div class="test_content_title">
                <h2>单选题</h2>
                <p>
                  <span>共</span><i class="content_lit">{{questionAlist.length}}</i><span>题，</span><span>每题</span><i
                  class="content_fs">{{questionAscore}}</i><span>分</span>
                </p>
              </div>
            </div>
            <div class="test_content_nr">
              <ul>
                <li v-for="(questionA, index) in questionAlist" :id="'qu_0_' + index">
                  <div class="test_content_nr_tt">
                    <i>{{index + 1}}</i><span>({{questionAscore}}分)</span>{{questionA.questionTitle}}<b
                    class="icon iconfont">&#xe881;</b>
                  </div>
                  <div class="test_content_nr_main">
                    <ul>
                      <li v-for="(option, optionIndex) in questionA.optionMaps" class="option">
                        <input type="radio" class="radioOrCheck" :name="'0_answer_' + index"
                               :id="'0_answer_' + index + '_option_' + optionIndex"
                        />
                        <label :for="'0_answer_' + index + '_option_' + optionIndex"
                               @click="setAnswer(0, index, option.k, 'A')">
                          {{option.k}}.
                          <p class="ue" style="display: inline;">{{option.v}}</p>
                        </label>
                      </li>
                    </ul>
                  </div>
                </li>
              </ul>
            </div>
            <div class="test_content">
              <div class="test_content_title">
                <h2>多选题</h2>
                <p>
                  <span>共</span><i class="content_lit">{{questionBlist.length}}</i><span>题，</span><span>每题</span><i
                  class="content_fs">{{questionBscore}}</i><span>分</span>
                </p>
              </div>
            </div>
            <div class="test_content_nr">
              <ul>
                <li v-for="(questionB, index) in questionBlist" :id="'qu_1_' + index">
                  <div class="test_content_nr_tt">
                    <i>{{index + 1}}</i><span>({{questionBscore}}分)</span>{{questionB.questionTitle}}<b
                    class="icon iconfont">&#xe881;</b>
                  </div>
                  <div class="test_content_nr_main">
                    <ul>
                      <li v-for="(option, optionIndex) in questionB.optionMaps" class="option">
                        <input type="checkbox" class="radioOrCheck" :name="'1_answer_' + index"
                               :id="'1_answer_' + index + '_option_' + optionIndex"
                        />
                        <label :for="'1_answer_' + index + '_option_' + optionIndex"
                               @click="setAnswer(1, index, '', 'B')">
                          {{option.k}}.
                          <p class="ue" style="display: inline;">{{option.v}}</p>
                        </label>
                      </li>
                    </ul>
                  </div>
                </li>
              </ul>
            </div>
            <div class="test_content">
              <div class="test_content_title">
                <h2>填空题</h2>
                <p>
                  <span>共</span><i class="content_lit">{{questionClist.length}}</i><span>题，</span><span>每题</span><i
                  class="content_fs">{{questionCscore}}</i><span>分</span>
                </p>
              </div>
            </div>
            <div class="test_content_nr">
              <ul>
                <li v-for="(questionC, index) in questionClist" :id="'qu_2_' + index">
                  <div class="test_content_nr_tt">
                    <i>{{index + 1}}</i><span>({{questionCscore}}分)</span>{{questionC.questionTitle}}<b
                    class="icon iconfont">&#xe881;</b>
                  </div>
                  <div class="test_content_nr_main">
                    <input type="text" :id="'2_answer_' + index" size="100%" :name="'2_answer_' + index"
                           v-on:input="setAnswer(2, index, '', 'C')"
                           style=
                             "border-color: #878787;
                      border-style: solid;
                      border-top-width: 0px;
                       border-right-width: 0px;
                      border-bottom-width: 1px;
                       border-left-width: 0px">
                  </div>
                </li>
              </ul>
            </div>
            <div class="test_content">
              <div class="test_content_title">
                <h2>判断题</h2>
                <p>
                  <span>共</span><i class="content_lit">{{questionDlist.length}}</i><span>题，</span><span>每题</span><i
                  class="content_fs">{{questionDscore}}</i><span>分</span>
                </p>
              </div>
            </div>
            <div class="test_content_nr">
              <ul>
                <li v-for="(questionD, index) in questionDlist" :id="'qu_3_' + index">
                  <div class="test_content_nr_tt">
                    <i>{{index + 1}}</i><span>({{questionDscore}}分)</span>{{questionD.questionTitle}}<b
                    class="icon iconfont">&#xe881;</b>
                  </div>
                  <div class="test_content_nr_main">
                    <ul>
                      <li class="option">
                        <input type="radio" class="radioOrCheck" value="1" :name="'3_answer_' + index"
                               :id="'3_answer_' + index + '_y'"
                        />
                        <label :for="'3_answer_' + index + '_y'" @click="setAnswer(3, index, '是', 'D')">
                          <p class="ue" style="display: inline;">是</p>
                        </label>
                      </li>
                      <li class="option">
                        <input type="radio" class="radioOrCheck" value="0" :name="'3_answer_' + index"
                               :id="'3_answer_' + index + '_n'"
                        />
                        <label :for="'3_answer_' + index + '_n'" @click="setAnswer(3, index, '否', 'D')">
                          <p class="ue" style="display: inline;">否</p>
                        </label>
                      </li>
                    </ul>
                  </div>
                </li>
              </ul>
            </div>
            <div class="test_content">
              <div class="test_content_title">
                <h2>简答题</h2>
                <p>
                  <span>共</span><i class="content_lit">{{questionElist.length}}</i><span>题，</span><span>每题</span><i
                  class="content_fs">{{questionEscore}}</i><span>分</span>
                </p>
              </div>
            </div>
            <div class="test_content_nr">
              <ul>
                <li v-for="(questionE, index) in questionElist" :id="'qu_4_' + index">
                  <div class="test_content_nr_tt">
                    <i>{{index + 1}}</i><span>({{questionEscore}}分)</span>{{questionE.questionTitle}}<b
                    class="icon iconfont">&#xe881;</b>
                  </div>
                  <div class="test_content_nr_main">
                    <input type="text" :id="'4_answer_' + index" size="100%" :name="'4_answer_' + index"
                           v-on:input="setAnswer(4, index, '', 'E')"
                           style=
                             "border-color: #878787;
                      border-style: solid;
                      border-top-width: 0px;
                       border-right-width: 0px;
                      border-bottom-width: 1px;
                       border-left-width: 0px">
                  </div>
                </li>
              </ul>
            </div>
          </form>
        </div>

      </div>
      <div class="nr_right">
        <div class="nr_rt_main">
          <div class="rt_nr1">
            <div class="rt_nr1_title">
              <h1>
                <i class="icon iconfont">&#xe692;</i>答题卡
              </h1>
              <p class="test_time">
                <i class="icon iconfont">&#xe6fb;</i><b class="alt-1">01:40</b>
              </p>
            </div>
            <div class="rt_content">
              <div class="rt_content_tt">
                <h2>单选题</h2>
                <p>
                  <span>共</span><i class="content_lit">{{questionAlist.length}}</i><span>题</span>
                </p>
              </div>
              <div class="rt_content_nr answerSheet">
                <ul>
                  <li v-for="(questionA, index) in questionAlist"><a :href="'#qu_0_' + index">{{index + 1}}</a></li>
                </ul>
              </div>
            </div>
            <div class="rt_content">
              <div class="rt_content_tt">
                <h2>多选题</h2>
                <p>
                  <span>共</span><i class="content_lit">{{questionBlist.length}}</i><span>题</span>
                </p>
              </div>
              <div class="rt_content_nr answerSheet">
                <ul>
                  <li v-for="(questionB, index) in questionBlist"><a :href="'#qu_1_' + index">{{index + 1}}</a></li>
                </ul>
              </div>
            </div>
            <div class="rt_content">
              <div class="rt_content_tt">
                <h2>填空题</h2>
                <p>
                  <span>共</span><i class="content_lit">{{questionClist.length}}</i><span>题</span>
                </p>
              </div>
              <div class="rt_content_nr answerSheet">
                <ul>
                  <li v-for="(questionC, index) in questionClist"><a :href="'#qu_2_' + index">{{index + 1}}</a></li>
                </ul>
              </div>
            </div>
            <div class="rt_content">
              <div class="rt_content_tt">
                <h2>判断题</h2>
                <p>
                  <span>共</span><i class="content_lit">{{questionDlist.length}}</i><span>题</span>
                </p>
              </div>
              <div class="rt_content_nr answerSheet">
                <ul>
                  <li v-for="(questionD, index) in questionDlist"><a :href="'#qu_3_' + index">{{index + 1}}</a></li>
                </ul>
              </div>
            </div>
            <div class="rt_content">
              <div class="rt_content_tt">
                <h2>简答题</h2>
                <p>
                  <span>共</span><i class="content_lit">{{questionElist.length}}</i><span>题</span>
                </p>
              </div>
              <div class="rt_content_nr answerSheet">
                <ul>
                  <li v-for="(questionE, index) in questionElist"><a :href="'#qu_4_' + index">{{index + 1}}</a></li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--nr end-->
    <div class="foot"></div>
  </div>
</template>

<script>
  import ElButton from "../../../admin-front/node_modules/element-ui/packages/button/src/button.vue";

  export default {
    components: {ElButton},
    data() {
      return {
        questionAscore: 5,
        questionBscore: 5,
        questionCscore: 5,
        questionDscore: 5,
        questionEscore: 20,
        questionAlist: [{
          id: 1,
          questionTitle: "2",
          optionMaps: [
            {k: "A", v: "1"},
            {k: "B", v: "2"},
            {k: "C", v: "3"},
            {k: "D", v: "4"}
          ],
          answer: "A",
        }, {
          id: 2,
          questionTitle: "2",
          optionMaps: [
            {k: "A", v: "1"},
            {k: "B", v: "2"},
            {k: "C", v: "3"},
            {k: "D", v: "4"}
          ],
          answer: "A",
        }, {
          id: 3,
          questionTitle: "2",
          optionMaps: [
            {k: "A", v: "1"},
            {k: "B", v: "2"},
            {k: "C", v: "3"},
            {k: "D", v: "4"}
          ],
          answer: "A",
        }],
        questionBlist: [{
          id: 1,
          questionTitle: "2",
          optionMaps: [
            {k: "A", v: "1"},
            {k: "B", v: "2"},
            {k: "C", v: "3"},
            {k: "D", v: "4"}
          ],
          answer: "AB",
        }, {
          id: 2,
          questionTitle: "2",
          optionMaps: [
            {k: "A", v: "1"},
            {k: "B", v: "2"},
            {k: "C", v: "3"},
            {k: "D", v: "4"}
          ],
          answer: "ABC",
        }, {
          id: 3,
          questionTitle: "2",
          optionMaps: [
            {k: "A", v: "1"},
            {k: "B", v: "2"},
            {k: "C", v: "3"},
            {k: "D", v: "4"}
          ],
          answer: "ABCD",
        }],
        questionClist: [{
          id: 1,
          questionTitle: "2()",
          answer: "A",
        }, {
          id: 2,
          questionTitle: "2()",
          answer: "A",
        }, {
          id: 3,
          questionTitle: "2()",
          answer: "A",
        }],
        questionDlist: [{
          id: 1,
          questionTitle: "2",
          answer: 1,
        }, {
          id: 2,
          questionTitle: "2",
          answer: 0,
        }],
        questionElist: [{
          id: 1,
          questionTitle: "2",
          answer: ""
        }, {
          id: 2,
          questionTitle: "2",
          answer: ""
        }],
        examForm: {
          questionAanswer: [],
          questionBanswer: [],
          questionCanswer: [],
          questionDanswer: [],
          questionEanswer: []
        },
        paperUrl: '/api/paperInfo',
        examUrl: '/api/exam'
      }
    },
    mounted: function () {
      const self = this;
      let examId = this.$route.query.examId;
      if (examId == null) {
        return;
      }
      self.$http.get(self.paperUrl, {params: {examId: examId}}).then((response) => {
        if (response.data.status == 0) {
          self.questionAscore = response.data.data.questionAscore;
          self.questionBscore = response.data.data.questionBscore;
          self.questionCscore = response.data.data.questionCscore;
          self.questionDscore = response.data.data.questionDscore;
          self.questionEscore = response.data.data.questionEscore;
          self.questionAlist = response.data.data.questionAlist;
          self.questionBlist = response.data.data.questionBlist;
          self.questionClist = response.data.data.questionClist;
          self.questionDlist = response.data.data.questionDlist;
          self.questionElist = response.data.data.questionElist;
          for (let i in self.questionAlist) {
            self.examForm.questionAanswer[i] = "";
          }
          for (let i in self.questionBlist) {
            self.examForm.questionBanswer[i] = "";
          }
          for (let i in self.questionClist) {
            self.examForm.questionCanswer[i] = "";
          }
          for (let i in self.questionDlist) {
            self.examForm.questionDanswer[i] = "";
          }
          for (let i in self.questionElist) {
            self.examForm.questionEanswer[i] = "";
          }
        } else if (response.data.status > 0) {
          self.$message.error("获取考试信息失败！" + response.data.msg);
        } else {
          self.$message.error("获取考试信息失败！请稍后重试或咨询管理员");
        }
      });
    },
    methods: {
      setAnswer(questionIndex, index, value, type) {
        if (type == 'A') {
          this.examForm.questionAanswer[index] = value;
        } else if (type == 'D') {
          this.examForm.questionDanswer[index] = value;
        }
        let cardLi = document.querySelector('a[href="#qu_' + questionIndex + '_' + index + '"]'); // 根据题目ID找到对应答题卡
        // 设置已答题
        if (cardLi == null) {
          return;
        }
        if (!cardLi.classList.contains('hasBeenAnswer')) {
          cardLi.classList.add('hasBeenAnswer');
        }
      },
      postAnswer() {
        this.$confirm('是否确认交卷?请检查是否有未完成试题', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          for (let i in this.questionBlist) {
            let obj = document.getElementsByName('1_answer_' + i);
            for (let k in obj) {
              if (obj[k].checked) this.examForm.questionBanswer[i] += k + ',';
            }
          }
          for (let i in this.questionClist) {
            this.examForm.questionCanswer[i] = document.getElementById('2_answer_' + i).value;
          }
          for (let i in this.questionElist) {
            this.examForm.questionEanswer[i] = document.getElementById('4_answer_' + i).value;
          }
          this.$http.post(this.examUrl, {params: this.examForm}).then((response) => {
            if (response.data.status == 0) {
              this.$alert("交卷成功！", "提示");
            } else if (response.data.status > 0) {
              self.$message.error("交卷失败！" + response.data.msg);
            } else {
              self.$message.error("交卷失败！请稍后重试或咨询管理员");
            }
          })
        }).catch(() => {
        });
      }
    }
  }
</script>

<style>
  @import '../assets/css/iconfont.css';
  @import '../assets/css/main.css';
  @import '../assets/css/test.css';

  .hasBeenAnswer {
    background: #5d9cec;
    color: #fff;
  }
</style>
