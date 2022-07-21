class forgotPass extends App{
    constructor() {
        super();
        this.input = {
            user_name: $('#forgot_pass_user'),
            real_otp: $('#realopt'),
            uotp: $('#uotp'),
            h_username: $('#h_username')
        };

            this.div = {
                result: $('#result'),
                container: $('#forgot-container'),
                after_otp: $('#forgot-after-otp'),
                change_pass: $('#change-password'),
            }
    }

    getPass(){
        let user_name = this.input.user_name.val();
        this.input.h_username.val(user_name);
        let result = this.div.result;
        let _this = this
        $.ajax({
            url:"http://127.0.0.1:8014/reset_password/",
            type:"get",
            data:{username:user_name},
            success:function(data) {
                if(data.status === "failed"){
                    result.html('<p>Kullanıcı Bulunamadı</p>')
                }else if(data.status === 'error'){
                    result.html(`${data.email} adresine mail gönderilemedi`)
                }else if(data.status === 'sent'){
                    result.html(`Yeni şifreniz email adresinize gönderilmiştir.`)
                    _this.div.container.hide();
                    _this.div.after_otp.slideDown(1000)
                    _this.input.real_otp.val(data.rotp)
                }
            }
        })
    };

    matchotp(){
        let uotp = this.input.uotp.val()
        let rotp = this.input.real_otp.val()

        if(uotp === rotp){
                this.div.after_otp.hide();
                this.div.change_pass.fadeIn(1000);
                this.div.result.html('<p>Şifre doğru</p>')
        }else{
            alert(' sifre yanlıs')

        }
    }
}

let forgot_pass = new forgotPass();