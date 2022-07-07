class App{
    constructor() {
        this.button = {
            navbar_user_btn : $('#user')
        }
    }
    ajaxRequest(url, data, cache = true, contentType = 'application/x-www-form-urlencoded; charset=UTF-8', processData = true) {
        return new Promise((resolve, reject) => {
            $.ajax({
                url: url,
                type: "POST",
                cache: cache,
                contentType: contentType,
                processData: processData,
                data: data,
                headers: token,
                success: function (data) {
                    resolve(data);
                },
                error: reject
            });
        });
    }
}

let app = new App();