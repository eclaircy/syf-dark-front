<template>
    <div>
        <dv-border-box-11 title="Rouge Killer" style="font-family:Times New Roman;height:400px;width:600px;z-index:0;position: absolute;margin: 125px 465px;"></dv-border-box-11>
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
              placeholder="Username"
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
        </el-form>
    </div>
</template>