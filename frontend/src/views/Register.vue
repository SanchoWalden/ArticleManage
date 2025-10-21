<template>
  <v-container fluid class="fill-height bg-gradient">
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="5">
        <v-card class="elevation-12">
          <v-card-title class="text-center bg-primary pa-6">
            <h2 class="text-white">注册新账号</h2>
          </v-card-title>

          <v-card-text class="pa-6">
            <v-form ref="formRef" v-model="valid" @submit.prevent="handleRegister">
              <v-text-field
                v-model="form.username"
                label="用户名"
                prepend-inner-icon="mdi-account"
                :rules="[rules.required, rules.username]"
                variant="outlined"
                class="mb-3"
              ></v-text-field>

              <v-text-field
                v-model="form.email"
                label="邮箱"
                prepend-inner-icon="mdi-email"
                :rules="[rules.required, rules.email]"
                variant="outlined"
                class="mb-3"
              ></v-text-field>

              <v-text-field
                v-model="form.password"
                label="密码"
                prepend-inner-icon="mdi-lock"
                :rules="[rules.required, rules.password]"
                :type="showPassword ? 'text' : 'password'"
                :append-inner-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append-inner="showPassword = !showPassword"
                variant="outlined"
                class="mb-3"
              ></v-text-field>

              <v-text-field
                v-model="form.confirmPassword"
                label="确认密码"
                prepend-inner-icon="mdi-lock-check"
                :rules="[rules.required, rules.confirmPassword]"
                :type="showConfirmPassword ? 'text' : 'password'"
                :append-inner-icon="showConfirmPassword ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append-inner="showConfirmPassword = !showConfirmPassword"
                variant="outlined"
                class="mb-3"
              ></v-text-field>

              <v-alert
                v-if="error"
                type="error"
                density="compact"
                class="mb-3"
              >
                {{ error }}
              </v-alert>

              <v-btn
                type="submit"
                color="primary"
                block
                size="large"
                :loading="loading"
                :disabled="!valid"
              >
                注册
              </v-btn>
            </v-form>
          </v-card-text>

          <v-card-actions class="pa-6 pt-0">
            <v-spacer></v-spacer>
            <v-btn
              text
              color="primary"
              @click="$router.push('/login')"
            >
              已有账号？去登录
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const formRef = ref(null)
const valid = ref(false)
const loading = ref(false)
const error = ref('')
const showPassword = ref(false)
const showConfirmPassword = ref(false)

const form = ref({
  username: '',
  email: '',
  password: '',
  confirmPassword: ''
})

const rules = {
  required: value => !!value || '此字段必填',
  username: value => {
    if (value?.length < 3) return '用户名至少3个字符'
    if (value?.length > 20) return '用户名最多20个字符'
    return true
  },
  email: value => {
    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return pattern.test(value) || '请输入有效的邮箱地址'
  },
  password: value => {
    if (value?.length < 6) return '密码至少6个字符'
    return true
  },
  confirmPassword: value => {
    return value === form.value.password || '两次密码输入不一致'
  }
}

const handleRegister = async () => {
  if (!valid.value) return

  loading.value = true
  error.value = ''

  const { confirmPassword, ...registerData } = form.value
  const result = await authStore.register(registerData)

  if (result.success) {
    router.push('/dashboard')
  } else {
    error.value = result.error
  }

  loading.value = false
}
</script>

<style scoped>
.bg-gradient {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
</style>
