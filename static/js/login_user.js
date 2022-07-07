class LoginUser extends App{
    constructor(props) {
        super(props);
        this.forms = {
            login: $('#user_login_form')
        };
        this.inputs = {
            username: $('#login_username'),
            password: $('#login_password'),
        };
        this.forms.login.submit(e => {
            e.preventDefault();
            this.loginSubmit();
        });

    }
    loginSubmit(){
        this.ajaxRequest('/login/', {username: this.inputs.username.val(), password: this.inputs.password.val()})
            .then(res => {
                res.status ? window.location.href = "/" : null;
            });
    }
}

let login_user = new LoginUser();