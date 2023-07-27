<template>
  <div class="login-container" :style="{ backgroundImage: 'url(' + bg + ')' }" >
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal"  @select="handleSelect">
      <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">插件</a></el-menu-item>
      <el-menu-item index="1">登录</el-menu-item>
      <el-menu-item  index="2" hidden>注册</el-menu-item >
      
    </el-menu>

    <el-main>
      <div v-if="activeIndex === '1'">
        <div style="text-align:center;">
          <div style="font-size:40px;color:white;font-family: SimSun;margin-top:80px;">软件下载网站检测与追踪溯源平台</div>
        </div>
        <dv-border-box-11 title="Rouge Killer" style="font-family:Times New Roman;height:380px;width:580px;z-index:0;position: absolute;margin: 30px 459px;"></dv-border-box-11>
        <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form" autocomplete="on" label-position="left">
          <div style="margin-bottom: 80px;" >
            <!-- <h3 class="title">Login </h3> -->
          </div>
          <el-form-item prop="username">
            <span class="svg-container">
              <svg-icon icon-class="user" />
            </span>
            <el-input
              ref="username"
              v-model="loginForm.username"
              placeholder="Username or Email"
              name="username"
              type="text"
              tabindex="1"
              autocomplete="on"
            />
          </el-form-item>
          <el-tooltip v-model="capsTooltip" content="Caps lock is On" placement="right" manual>
            <el-form-item prop="password">
              <span class="svg-container">
                <svg-icon icon-class="password" />
              </span>
              <el-input
                :key="passwordType"
                ref="password"
                v-model="loginForm.password"
                :type="passwordType"
                placeholder="Password"
                name="password"
                tabindex="2"
                autocomplete="on"
                @keyup.native="checkCapslock"
                @blur="capsTooltip = false"
                @keyup.enter.native="handleLogin"
              />
              <span class="show-pwd" @click="showPwd">
                <svg-icon :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'" />
              </span>
            </el-form-item>
          </el-tooltip>
          <ParticleEffectButton :loading="loading"    @click.native.prevent="handleLogin"
              :visible.sync="btnOps.visible" :animating.sync="btnOps.animating" :options="btnOps" cls="btn-cls" style="">
              <span style="font-family:Times New Roman;margin-left: -16px;margin-top: -11px; z-index: 2;font-size: larger; position: absolute;">Login</span>
          </ParticleEffectButton>
          <div style="float:right;font-weight:500;margin-top:20px;">
            <el-link type="primary" @click="showRegister"><span style="color:#b1b8be">New User? </span>Sign up</el-link>
          </div>
        </el-form>
      </div>
      <div v-if="activeIndex === '2'">
        <div style="text-align:center;">
          <div style="font-size:40px;color:white;font-family: SimSun;margin-top:80px;">软件下载网站检测与追踪溯源平台</div>
        </div>
        <dv-border-box-11 title="Rouge Killer" style="font-family:Times New Roman;height:380px;width:580px;z-index:0;position: absolute;margin: 30px 459px;"></dv-border-box-11>
        <el-form ref="registerForm" :model="registerForm" :rules="registerRules" class="login-form" label-position="left">
          <div style="margin-bottom: 65px;" >
          </div>

          <el-form-item prop="username">
            <span class="svg-container"> <svg-icon icon-class="user" /> </span>
            <el-input ref="username" v-model="registerForm.username" placeholder="Username"  type="text" tabindex="1" />
          </el-form-item>
         
          <el-form-item prop="password">
            <span class="svg-container"> <svg-icon icon-class="password" /> </span>
            <el-input  :key="passwordType" ref="password" v-model="registerForm.password" :type="passwordType"
              placeholder="Password"  name="password"  tabindex="2"/>
            <span class="show-pwd" @click="showPwd">
              <svg-icon :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'" />
            </span>
          </el-form-item>

          <el-form-item prop="email">
            <span class="svg-container">   <svg-icon icon-class="email" />  </span>
            <el-input ref="email" v-model="registerForm.email" placeholder="Email" name="email" type="text" tabindex="3"/>
          </el-form-item>

          <div style="font-weight:500;margin-top:20px;">
            <el-button @click="handleRegister" style="float:right;">Register</el-button>
            <el-link style="float:left;" type="primary" @click="showLogin"><span style="color:#b1b8be">Already have account? </span>Sign in</el-link>
          </div>
        </el-form>
      </div>
      
    </el-main>
  </div>
</template>

<script>
import { validUsername } from '@/utils/validate'
import SocialSign from './components/SocialSignin'
import ParticleEffectButton from "vue-particle-effect-buttons"


export default {
  name: 'Login',
  components: { SocialSign,ParticleEffectButton },
  data() {
    const validateUsername = (rule, value, callback) => {
      if (!validUsername(value)) {
        callback(new Error('Please enter the correct user name'))
      } else {
        callback()
      }
    }
    const validatePassword = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error('密码长度不能少于6位数'))
      } else {
        callback()
      }
    }
    return {
      activeIndex: '1',
      loginForm: {
        username: '',
        password: ''
      },
      loginRules: {
        username: [{ required: true, trigger: 'blur', }],
        password: [{ required: true, trigger: 'blur' }]
      },
      passwordType: 'password',
      capsTooltip: false,
      loading: false,
      showDialog: false,
      redirect: undefined,
      otherQuery: {},
      btnOps: {
          type: "triangle",
          easing: "easeOutQuart",
          size: 6,
          particlesAmountCoefficient: 4,
          oscillationCoefficient: 2,
          color: function() {
              return Math.random() < 0.5 ? "#000000" : "#ffffff";
          },
          onComplete: () => {
            console.log("complete");
          },
          onBegin: () => {
            console.log("begin");
          },
          visible: true,
          animating: false
      },
      bg: require('@/assets/bg/bg.jpg'),
      registerForm:{
        username: '',
        email: '',
        password: '',
        role:'',
      },
      registerRules:{
        username: [{ required: true, trigger: 'blur', message: '请输入用户名',}],
        password: [{ required: true, trigger: 'blur', validator: validatePassword }],
        email: [{ required: true, message: '请输入邮箱地址', trigger: 'blur' },
                { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur'] }],
      },
      roleType:{
        "2":"执法人员",
        "3":"普通用户",
      }
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        const query = route.query
        if (query) {
          this.redirect = query.redirect
          this.otherQuery = this.getOtherQuery(query)
        }
      },
      immediate: true
    },
    activeIndex(newVal,oldVal){
      if(newVal == '2'){
        this.$refs["registerForm"].resetFields();
        this.$refs["registerForm"].clearValidate();
      }
    }
  },
  created() {
    // window.addEventListener('storage', this.afterQRScan)
  },
  mounted() {
    if (this.loginForm.username === '') {
      this.$refs.username.focus()
    } else if (this.loginForm.password === '') {
      this.$refs.password.focus()
    }
  },
  destroyed() {
    // window.removeEventListener('storage', this.afterQRScan)
  },
  methods: {
    handleSelect(index) {
      this.activeIndex = index;
      // 在这里你可以根据需要进行其他的处理逻辑
    },
    showRegister(){
      this.activeIndex = '2';
    },
    showLogin(){
      this.activeIndex = '1';
    },
    checkCapslock(e) {
      const { key } = e
      this.capsTooltip = key && key.length === 1 && (key >= 'A' && key <= 'Z')
    },
    showPwd() {
      if (this.passwordType === 'password') {
        this.passwordType = ''
      } else {
        this.passwordType = 'password'
      }
      this.$nextTick(() => {
        this.$refs.password.focus()
      })
    },
    handleLogin() {
      this.$refs.loginForm.validate(valid => {
        if (valid) {
          this.loading = true
          // let fd = new FormData()
          // fd.append("username", this.loginForm.username)
          // fd.append("password", this.loginForm.password)
          // this.axios.post('http://127.0.0.1:8888/user/login', fd,{ headers: {'Content-Type': 'multipart/form-data'}})
          // .then(res => {
          //   if(res.data==true){ //login success
          //       this.$message({
          //         message: ' 登录成功',
          //         type: 'success'
          //       });
          //       setTimeout(() => {
          //         this.$router.push({ path: this.redirect || '/dashboard', query: this.otherQuery })
          //         this.loading = false
          //       }, 1 * 1000)
          //   }else{
          //     this.loading = false
          //     this.$message.error('登陆失败，用户名密码不匹配');
          //     setTimeout(() => {
          //       this.btnOps.visible = !this.btnOps.visible;
          //     }, 2.5 * 1000)
          //   } 
          // })


          this.$store.dispatch('user/login', this.loginForm)
            .then(() => {
              this.$message({
                message: ' 登录成功',
                type: 'success'
              });
              setTimeout(() => {
                this.$router.push({ path: this.redirect || '/dashboard', query: this.otherQuery })
                this.loading = false
              }, 1 * 1000)
            })
            .catch(() => {
              this.loading = false
            })
        } else {
          this.$message.error('登陆失败，请正确填写表单');
          // wait until this.btnOps.animating is false then set this.btnOps.visible to true
          setTimeout(() => {
            this.btnOps.visible = !this.btnOps.visible;
          }, 2.5 * 1000)
          
          return false
        }
      })
    },
    handleRegister(){
      this.$refs.registerForm.validate(valid => {
        if (valid) {
            this.$message({
              message: '账号注册成功',
              type: 'success'
            });
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    getOtherQuery(query) {
      return Object.keys(query).reduce((acc, cur) => {
        if (cur !== 'redirect') {
          acc[cur] = query[cur]
        }
        return acc
      }, {})
    }
    // afterQRScan() {
    //   if (e.key === 'x-admin-oauth-code') {
    //     const code = getQueryObject(e.newValue)
    //     const codeMap = {
    //       wechat: 'code',
    //       tencent: 'code'
    //     }
    //     const type = codeMap[this.auth_type]
    //     const codeName = code[type]
    //     if (codeName) {
    //       this.$store.dispatch('LoginByThirdparty', codeName).then(() => {
    //         this.$router.push({ path: this.redirect || '/' })
    //       })
    //     } else {
    //       alert('第三方登录失败')
    //     }
    //   }
    // }
  }
}
</script>

<style lang="scss">
/* 修复input 背景不协调 和光标变色 */
/* Detail see https://github.com/PanJiaChen/vue-element-admin/pull/927 */

$bg:#283443;
$light_gray:#fff;
$cursor: #fff;

@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .login-container .el-input input {
    color: $cursor;
  }
}

/* reset element-ui css */
.login-container {
  .el-input {
    display: inline-block;
    height: 47px;
    width: 85%;

    input {
      background: transparent;
      border: 0px;
      -webkit-appearance: none;
      border-radius: 0px;
      padding: 12px 5px 12px 15px;
      color: $light_gray;
      height: 47px;
      caret-color: $cursor;

      &:-webkit-autofill {
        box-shadow: 0 0 0px 1000px $bg inset !important;
        -webkit-text-fill-color: $cursor !important;
      }
    }
  }

  .el-form-item {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    color: #454545;
  }
}
</style>

<style lang="scss" scoped>
$bg:#2d3a4b;
$dark_gray:#889aa4;
$light_gray:#eee;

.login-container {
  min-height: 100%;
  width: 100%;

  overflow: hidden;
  background-size:100% 100%;

  .login-form {
    position: relative;
    width: 520px;
    max-width: 100%;
    padding: 50px 40px 0;
    margin: 0 auto;
    overflow: hidden;
  }

  .tips {
    font-size: 14px;
    color: #fff;
    margin-bottom: 10px;

    span {
      &:first-of-type {
        margin-right: 16px;
      }
    }
  }

  .svg-container {
    padding: 6px 5px 6px 15px;
    color: $dark_gray;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }

  .title-container {
    position: relative;

    .title {
      font-size: 26px;
      color: $light_gray;
      margin: 0px auto 40px auto;
      text-align: center;
      font-weight: bold;
    }
  }

  .show-pwd {
    position: absolute;
    right: 10px;
    top: 7px;
    font-size: 16px;
    color: $dark_gray;
    cursor: pointer;
    user-select: none;
  }

  .thirdparty-button {
    position: absolute;
    right: 0;
    bottom: 6px;
  }

  @media only screen and (max-width: 470px) {
    .thirdparty-button {
      display: none;
    }
  }
}

</style>

<style scoped>
/deep/.vue-particle-effect-button .particles-button {
  background: #f1f1f47d;
  width:438.4px;
  height:40px;
  color: #4545f37d;
  text-align: center;
}

/deep/.el-menu {
  background-color: transparent;
}
/deep/.el-menu.el-menu--horizontal {
  border-bottom: transparent; 
}
/deep/.el-menu > .el-menu-item {
  float: right;
}
/deep/.el-menu > .el-menu-item:hover {
  background-color: transparent;
}
</style>
