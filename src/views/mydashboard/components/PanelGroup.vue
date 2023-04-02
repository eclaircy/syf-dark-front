<template>
  <el-row :gutter="40" class="panel-group">
    <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
      <div class="card-panel" @click="handleSetLineChartData('newVisitis')">
        <div class="card-panel-icon-wrapper icon-people">
          <svg-icon icon-class="peoples" class-name="card-panel-icon" />
        </div>
        <div class="card-panel-description">
          <div class="card-panel-text">
            下载网站总数
          </div>
          <count-to :start-val="0" :end-val="102400" :duration="2600" class="card-panel-num" />
        </div>
      </div>
    </el-col>
    <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
      <div class="card-panel" @click="handleSetLineChartData('messages')">
        <div class="card-panel-icon-wrapper icon-message">
          <svg-icon icon-class="message" class-name="card-panel-icon" />
        </div>
        <div class="card-panel-description">
          <div class="card-panel-text">
            恶意下载网站
          </div>
          <count-to :start-val="0" :end-val="81212" :duration="3000" class="card-panel-num" />
        </div>
      </div>
    </el-col>
    <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
      <div class="card-panel" @click="handleSetLineChartData('purchases')">
        <div class="card-panel-icon-wrapper icon-money">
          <!-- <i class="el-icon-s-flag" /> -->
          <svg-icon icon-class="money" class-name="card-panel-icon" />
          <!-- <svg t="1680003704116" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2712" width="200" height="200"><path d="M376.967 345.239h56.905v258.789h-56.905zM540.793 511.24h59.805c16.186 0 29.958-2.356 41.319-7.067 11.354-4.712 20.597-10.93 27.727-18.667 7.125-7.73 12.323-16.61 15.586-26.64 3.262-10.024 4.893-20.235 4.893-30.627 0-10.63-1.631-20.897-4.893-30.808-3.263-9.905-8.461-18.723-15.586-26.459-7.13-7.73-16.372-13.954-27.727-18.666-11.361-4.712-25.134-7.068-41.319-7.068H483.889v258.789h56.904V511.24z m0-121.782h44.219c6.524 0 12.805 0.487 18.848 1.45 6.037 0.969 11.354 2.843 15.948 5.618 4.587 2.781 8.273 6.705 11.055 11.779 2.774 5.075 4.168 11.723 4.168 19.935 0 8.217-1.394 14.86-4.168 19.935-2.781 5.074-6.468 9.004-11.055 11.78-4.594 2.78-9.911 4.655-15.948 5.618-6.043 0.968-12.323 1.45-18.848 1.45h-44.219v-77.565z" fill="#d81e06" p-id="2713"></path><path d="M864 128.542H159c-17.673 0-32 14.327-32 32v598.979c0 17.673 14.327 32 32 32h321v115.522c0 17.673 14.327 32 32 32 17.673 0 32-14.327 32-32V791.521h320c17.673 0 32-14.327 32-32V160.542c0-17.673-14.327-32-32-32z m-32 598.979H191V192.542h641v534.979z" fill="#d81e06" p-id="2714"></path></svg> -->
        </div>
        <div class="card-panel-description">
          <div class="card-panel-text">
            恶意IP
          </div>
          <count-to :start-val="0" :end-val="9280" :duration="3200" class="card-panel-num" />
        </div>
      </div>
    </el-col>
    <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
      <div class="card-panel" @click="handleSetLineChartData('shoppings')">
        <div class="card-panel-icon-wrapper icon-shopping">
          <svg-icon icon-class="shopping" class-name="card-panel-icon" />
        </div>
        <div class="card-panel-description">
          <div class="card-panel-text">
            恶意团伙
          </div>
          <count-to :start-val="0" :end-val="13600" :duration="3600" class="card-panel-num" />
        </div>
      </div>
    </el-col>
  </el-row>
</template>

<script>
import CountTo from 'vue-count-to'

export default {
  components: {
    CountTo
  },
  methods: {
    handleSetLineChartData(type) {
      this.$emit('handleSetLineChartData', type)
    }
  }
}
</script>

<style lang="scss" scoped>
.panel-group {
  margin-top: 18px;

  .card-panel-col {
    margin-bottom: 32px;
  }

  .card-panel {
    height: 108px;
    cursor: pointer;
    font-size: 12px;
    position: relative;
    overflow: hidden;
    color: #666;
    background: #fff;
    box-shadow: 4px 4px 40px rgba(0, 0, 0, .05);
    border-color: rgba(0, 0, 0, .05);

    &:hover {
      .card-panel-icon-wrapper {
        color: #fff;
      }

      .icon-people {
        background: #40c9c6;
      }

      .icon-message {
        background: #36a3f7;
      }

      .icon-money {
        background: #f4516c;
      }

      .icon-shopping {
        background: #34bfa3
      }
    }

    .icon-people {
      color: #40c9c6;
    }

    .icon-message {
      color: #36a3f7;
    }

    .icon-money {
      color: #f4516c;
    }

    .icon-shopping {
      color: #34bfa3
    }

    .card-panel-icon-wrapper {
      float: left;
      margin: 14px 0 0 14px;
      padding: 16px;
      transition: all 0.38s ease-out;
      border-radius: 6px;
    }

    .card-panel-icon {
      float: left;
      font-size: 48px;
    }

    .card-panel-description {
      float: right;
      font-weight: bold;
      margin: 26px;
      margin-left: 0px;

      .card-panel-text {
        line-height: 18px;
        color: rgba(0, 0, 0, 0.45);
        font-size: 16px;
        margin-bottom: 12px;
      }

      .card-panel-num {
        font-size: 20px;
      }
    }
  }
}

@media (max-width:550px) {
  .card-panel-description {
    display: none;
  }

  .card-panel-icon-wrapper {
    float: none !important;
    width: 100%;
    height: 100%;
    margin: 0 !important;

    .svg-icon {
      display: block;
      margin: 14px auto !important;
      float: none !important;
    }
  }
}
</style>
