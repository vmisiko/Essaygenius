const validationMxn = {
    data() {
        return{
            emailRules: [
                (v) => !!v || "Email is required",
                (v) => /.+@.+/.test(v) || 'E-mail must be valid',
            ],
            passwordRules: [
                (v) => !!v || "password is required",
            ],
        }
    }
};

export default validationMxn;