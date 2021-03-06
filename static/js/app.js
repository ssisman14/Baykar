class App{
    constructor() {
        this.button = {
            navbar_user_btn : $('#user')
        }
        this.api_url = {
            ilan : 'http://127.0.0.1:8014/api/ilan/?format=json',
            create_ilan :'http://127.0.0.1:8014/api/ilan/',
            ilan_yayinlayan_filter: `http://127.0.0.1:8014/api/ilan/?format=json&yayinlayan=${user_id}`,
            company: 'http://127.0.0.1:8014/api/company/?format=json',
            ilan_kullanici: 'http://127.0.0.1:8014/api/related_aday_ilan/',
        }
    }
    ajaxRequest(url, data,type, cache = true, contentType = 'application/x-www-form-urlencoded; charset=UTF-8', processData = true) {
        return new Promise((resolve, reject) => {
            $.ajax({
                url: url,
                type: type,
                cache: cache,
                headers: token,
                contentType: contentType,
                processData: processData,
                data: data,
                success: function (data) {
                    resolve(data);
                },
                error: reject
            });
        });
    }
}

let app = new App();