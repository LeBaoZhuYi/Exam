<template>
    <my-page title="HTML">
      <div>
        <mu-table :fixedFooter="fixedFooter" :fixedHeader="fixedHeader" :height="height"
                  :enableSelectAll="enableSelectAll" :multiSelectable="multiSelectable"
                  :selectable="selectable" :showCheckbox="showCheckbox">
          <mu-thead slot="header">
            <mu-tr>
              <mu-th tooltip="ID">ID</mu-th>
              <mu-th tooltip="名称">Name</mu-th>
              <mu-th tooltip="状态">Status</mu-th>
            </mu-tr>
          </mu-thead>
          <mu-tbody>
            <mu-tr v-for="item,index in tableData"  :key="index" :selected="item.selected">
              <mu-td>{{index + 1}}</mu-td>
              <mu-td>{{item.name}}</mu-td>
              <mu-td>{{item.status}}</mu-td>
            </mu-tr>
          </mu-tbody>
          <mu-tfoot slot="footer">
            <mu-tr>
              <mu-td>ID</mu-td>
              <mu-td>Name</mu-td>
              <mu-td>Status</mu-td>
            </mu-tr>
          </mu-tfoot>
        </mu-table>
        <div class="demo-table-settings">
          <h3>设置</h3>
          <mu-text-field v-model.lazy="height" label="table的高度"/><br/>
          <mu-switch labelLeft label="固定表头" v-model="fixedHeader"/><br/>
          <mu-switch labelLeft label="固定表尾" v-model="fixedFooter"/><br/>
          <mu-switch labelLeft label="可以被选择" v-model="selectable"/><br/>
          <mu-switch labelLeft label="可以多选" v-model="multiSelectable"/><br/>
          <mu-switch labelLeft label="可以选择全部" v-model="enableSelectAll"/><br/>
          <mu-switch labelLeft label="显示复选框" v-model="showCheckbox"/><br/>
        </div>
      </div>
    </my-page>
</template>
<script>
  export default {
    data () {
      return {
        tableData: [
          {
            name: 'John Smith',
            status: 'Employed',
            selected: true
          },
          {
            name: 'Randal White',
            status: 'Unemployed'
          },
          {
            name: 'Stephanie Sanders',
            status: 'Employed',
            selected: true
          },
          {
            name: 'Steve Brown',
            status: 'Employed'
          },
          {
            name: 'Joyce Whitten',
            status: 'Employed'
          },
          {
            name: 'Samuel Roberts',
            status: 'Employed'
          },
          {
            name: 'Adam Moore',
            status: 'Employed'
          }
        ],
        fixedHeader: true,
        fixedFooter: true,
        selectable: true,
        multiSelectable: true,
        enableSelectAll: false,
        showCheckbox: true,
        height: '300px'
      }
    }
  }
</script>


<style lang="scss" scoped>

  .demo-table-settings{
    width: 200px;
    overflow: hidden;
    margin: 20px auto 0px;
  }
    .ui-medal {
        width: 282px;
        height: 375px;
        background-color: #fff;
        border: 1px solid #f00;
        text-align: center;
        .medal-content {
            width: 100%;
            position: relative;
            height: 200px;
            padding-top: 40px;
        }
        .number {
            position: absolute;
            left: 50%;
            bottom: -25px;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            color: #fff;
            background-color: #31a56e;
            text-align: center;
            line-height: 50px;
            border: 2px solid #fff;
            margin-left: -25px;
        }
        .big {
            font-size: 30px;
        }
        .medal-img {
            width: 96px;
        }
        .medal-footer {
            width: 100%;
            height: 174px;
            padding-top: 50px;
            color: #fff;
            background-image: url("/static/img/medal-footer.png");
            background-size: 100% 100%;
            .title {
                margin-bottom: 28px;
                font-size: 18px;
            }
            .content {
            }
        }
    }

</style>
