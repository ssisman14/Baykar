class Main_Page extends App{
    constructor() {
        super();
        this.search_btn ={
            ilan_count : $('#ilan_count')
        }
        this.search();
    }
    search(){
        this.ajaxRequest(this.api_url.ilan ,{},'GET')
            .then(res=> {
                    this.search_btn.ilan_count.text(res.length);
                    console.log( this.search_btn.ilan_count);
                }
            )

    }
}

let main_page = new Main_Page()