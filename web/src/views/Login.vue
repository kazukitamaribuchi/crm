<template>
    <div id="login_wrap">
        <b-card
            title="Login"
            class="login_card"
        >
            <b-form>
                <b-form-group
                    class="login_input"
                >
                    <b-input-group>
                        <b-input-group-prepend is-text>
                            <b-icon icon="person-fill"></b-icon>
                        </b-input-group-prepend>
                        <b-form-input
                            v-model="credentials.username"
                            type="text"
                            placeholder="username"
                            required
                        ></b-form-input>
                    </b-input-group>
                </b-form-group>

                <b-form-group
                    class="password_input mt-3 mb-3"
                >
                    <b-input-group>
                        <b-input-group-prepend is-text>
                            <b-icon icon="lock-fill"></b-icon>
                        </b-input-group-prepend>
                        <b-form-input
                            v-model="credentials.password"
                            type="password"
                            placeholder="password"
                            required
                        ></b-form-input>
                    </b-input-group>
                </b-form-group>

                <b-button
                    block
                    variant="primary"
                    class="submit_btn"
                    @click="login"
                >Login</b-button>
            </b-form>
        </b-card>
    </div>

</template>

<script>
import { mapActions } from 'vuex'

export default {
    name: 'LoginItem',
    data: () => ({
        credentials: {},
    }),
    created () {
        this.$axios({
            method: 'GET',
            url: 'api/customer/',
        })
        .then(res => {
            console.log(res)
        })
        .catch(e => {
            console.log(e)
        })
    },
    methods: {
        ...mapActions([
            'checkAuthToken',
        ]),
        login () {
            this.checkAuthToken(this.credentials)
            .then(res => {
                this.credentials = {}
                this.$router.push({name: 'Home'})
            })
            .catch(e => {
                console.log(e)
            })
        },
    }
}
</script>

<style lang="scss" scoped>
#login_wrap {
    height: 100%;
    padding-top: 15rem;
    // font-family: Hiragino Kaku Gothic Pro,ヒラギノ角ゴ Pro,Yu Gothic Medium,游ゴシック Medium,YuGothic,游ゴシック体,メイリオ,sans-serif;

    // background-color: $theme-color;
    background-color: $theme-color2;

    .input-group-text {
        height: 100%;
        border-radius: 5px 0 0 5px !important;
    }

    .card-title {
        text-align: center;
        font-size: 20px;
        margin: 40px auto 30px;
        // color: white;
    }

    .card-body {
        padding: 0.5rem 3rem;
    }

    .login_card {
        width: 500px;
        margin: 0 auto;

        // background-color: $theme-color2;
    }

    .submit_btn {
        margin: 1.5rem auto 2rem;
        width: 40%;
        display: block;
    }
}
</style>
