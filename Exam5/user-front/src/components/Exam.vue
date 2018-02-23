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
              <font><input type="button" name="test_jiaojuan" value="交卷"></font>
            </div>

            <div class="test_content">
              <div class="test_content_title">
                <h2>单选题</h2>
                <p>
                  <span>共</span><i class="content_lit">{{questionAList.length}}</i><span>题，</span><span>每题</span><i
                  class="content_fs">{{questionAScore}}</i><span>分</span>
                </p>
              </div>
            </div>
            <div class="test_content_nr">
              <ul>
                <li v-for="(questionA, index) in questionAList" :id="'qu_0_' + index">
                  <div class="test_content_nr_tt">
                    <i>{{index + 1}}</i><span>({{questionAScore}}分)</span>{{questionA.questionTitle}}<b
                    class="icon iconfont">&#xe881;</b>
                  </div>
                  <div class="test_content_nr_main">
                    <ul>
                      <li v-for="(option, optionIndex) in questionA.optionMaps" class="option">
                        <input type="radio" class="radioOrCheck" :name="'0_answer_' + index"
                               :id="'0_answer_' + index + '_option_' + optionIndex"
                        />
                        <label :for="'0_answer_' + index + '_option_' + optionIndex"
                               @click="addHasBeenAnswer(0, index)">
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
                  <span>共</span><i class="content_lit">{{questionBList.length}}</i><span>题，</span><span>每题</span><i
                  class="content_fs">{{questionBScore}}</i><span>分</span>
                </p>
              </div>
            </div>
            <div class="test_content_nr">
              <ul>
                <li v-for="(questionB, index) in questionBList" :id="'qu_1_' + index">
                  <div class="test_content_nr_tt">
                    <i>{{index + 1}}</i><span>({{questionBScore}}分)</span>{{questionB.questionTitle}}<b
                    class="icon iconfont">&#xe881;</b>
                  </div>
                  <div class="test_content_nr_main">
                    <ul>
                      <li v-for="(option, optionIndex) in questionB.optionMaps" class="option">
                        <input type="checkbox" class="radioOrCheck" :name="'1_answer_' + index"
                               :id="'1_answer_' + index + '_option_' + optionIndex"
                        />
                        <label :for="'1_answer_' + index + '_option_' + optionIndex"
                               @click="addHasBeenAnswer(1, index)">
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
                  <span>共</span><i class="content_lit">{{questionCList.length}}</i><span>题，</span><span>每题</span><i
                  class="content_fs">{{questionCScore}}</i><span>分</span>
                </p>
              </div>
            </div>
            <div class="test_content_nr">
              <ul>
                <li v-for="(questionC, index) in questionCList" :id="'qu_2_' + index">
                  <div class="test_content_nr_tt">
                    <i>{{index + 1}}</i><span>({{questionCScore}}分)</span>{{questionC.questionTitle}}<b
                    class="icon iconfont">&#xe881;</b>
                  </div>
                  <div class="test_content_nr_main">
                    <input type="text" :id="'2_answer_' + index" size="100%" :name="'2_answer_' + index"
                           v-on:input="addHasBeenAnswer(2, index)"
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
                  <span>共</span><i class="content_lit">{{questionDList.length}}</i><span>题，</span><span>每题</span><i
                  class="content_fs">{{questionDScore}}</i><span>分</span>
                </p>
              </div>
            </div>
            <div class="test_content_nr">
              <ul>
                <li v-for="(questionD, index) in questionDList" :id="'qu_3_' + index">
                  <div class="test_content_nr_tt">
                    <i>{{index + 1}}</i><span>({{questionDScore}}分)</span>{{questionD.questionTitle}}<b
                    class="icon iconfont">&#xe881;</b>
                  </div>
                  <div class="test_content_nr_main">
                    <ul>
                      <li class="option">
                        <input type="radio" class="radioOrCheck" value="1" :name="'3_answer_' + index"
                               :id="'3_answer_' + index + '_y'"
                        />
                        <label :for="'3_answer_' + index + '_y'" @click="addHasBeenAnswer(3, index)">
                          <p class="ue" style="display: inline;">是</p>
                        </label>
                      </li>
                      <li class="option">
                        <input type="radio" class="radioOrCheck" value="0" :name="'3_answer_' + index"
                               :id="'3_answer_' + index + '_n'"
                        />
                        <label :for="'3_answer_' + index + '_n'" @click="addHasBeenAnswer(3, index)">
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
                  <span>共</span><i class="content_lit">{{questionEList.length}}</i><span>题，</span><span>每题</span><i
                  class="content_fs">{{questionEScore}}</i><span>分</span>
                </p>
              </div>
            </div>
            <div class="test_content_nr">
              <ul>
                <li v-for="(questionE, index) in questionEList" :id="'qu_4_' + index">
                  <div class="test_content_nr_tt">
                    <i>{{index + 1}}</i><span>({{questionEScore}}分)</span>{{questionE.questionTitle}}<b
                    class="icon iconfont">&#xe881;</b>
                  </div>
                  <div class="test_content_nr_main">
                    <input type="text" :id="'4_answer_' + index" size="100%" :name="'4_answer_' + index"
                           v-on:input="addHasBeenAnswer(4, index)"
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
                  <span>共</span><i class="content_lit">{{questionAList.length}}</i><span>题</span>
                </p>
              </div>
              <div class="rt_content_nr answerSheet">
                <ul>
                  <li v-for="(questionA, index) in questionAList"><a :href="'#qu_0_' + index">{{index + 1}}</a></li>
                </ul>
              </div>
            </div>
            <div class="rt_content">
              <div class="rt_content_tt">
                <h2>多选题</h2>
                <p>
                  <span>共</span><i class="content_lit">{{questionBList.length}}</i><span>题</span>
                </p>
              </div>
              <div class="rt_content_nr answerSheet">
                <ul>
                  <li v-for="(questionB, index) in questionBList"><a :href="'#qu_1_' + index">{{index + 1}}</a></li>
                </ul>
              </div>
            </div>
            <div class="rt_content">
              <div class="rt_content_tt">
                <h2>填空题</h2>
                <p>
                  <span>共</span><i class="content_lit">{{questionCList.length}}</i><span>题</span>
                </p>
              </div>
              <div class="rt_content_nr answerSheet">
                <ul>
                  <li v-for="(questionC, index) in questionCList"><a :href="'#qu_2_' + index">{{index + 1}}</a></li>
                </ul>
              </div>
            </div>
            <div class="rt_content">
              <div class="rt_content_tt">
                <h2>判断题</h2>
                <p>
                  <span>共</span><i class="content_lit">{{questionDList.length}}</i><span>题</span>
                </p>
              </div>
              <div class="rt_content_nr answerSheet">
                <ul>
                  <li v-for="(questionD, index) in questionDList"><a :href="'#qu_3_' + index">{{index + 1}}</a></li>
                </ul>
              </div>
            </div>
            <div class="rt_content">
              <div class="rt_content_tt">
                <h2>简答题</h2>
                <p>
                  <span>共</span><i class="content_lit">{{questionEList.length}}</i><span>题</span>
                </p>
              </div>
              <div class="rt_content_nr answerSheet">
                <ul>
                  <li v-for="(questionE, index) in questionEList"><a :href="'#qu_4_' + index">{{index + 1}}</a></li>
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
  export default {
    data() {
      return {
        questionAScore: 5,
        questionBScore: 5,
        questionCScore: 5,
        questionDScore: 5,
        questionEScore: 20,
        questionAList: [{
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
        questionBList: [{
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
        questionCList: [{
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
        questionDList: [{
          id: 1,
          questionTitle: "2",
          answer: 1,
        }, {
          id: 2,
          questionTitle: "2",
          answer: 0,
        }],
        questionEList: [{
          id: 1,
          questionTitle: "2",
          answer: ""
        }, {
          id: 2,
          questionTitle: "2",
          answer: ""
        }]
      }
    },

    methods: {
      addHasBeenAnswer(questionIndex, index) {
        let cardLi = document.querySelector('a[href="#qu_' + questionIndex + '_' + index + '"]'); // 根据题目ID找到对应答题卡
        // 设置已答题
        if (cardLi == null) {
          return;
        }
        if (!cardLi.classList.contains('hasBeenAnswer')) {
          cardLi.classList.add('hasBeenAnswer');
        }
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
