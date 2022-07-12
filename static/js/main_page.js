class Main_Page extends App{
    constructor() {
        super();
        this.divs = {
            ilanlar: $('#ilanlar'),
        };
        this.search_btn ={
            ilan_count : $('#ilan_count'),
            filter : $('#filters-ilan')
        };
        this.inputs = {
            type: $('#filters_type'),
            city: $('#filters_city')
        }
        this.modal = {
            detay : {
                main: $('#ilan_detay_modal'),
                title: $('#ilan_title_detay'),
                company: $('#ilan_company_detay'),
                type: $('#ilan_type_detay'),
                city: $('#ilan_city_detay'),
                desc : $('#ilan_desc_detay'),
                close: $('#modal_detay_close')

            }
        }
        this.user_advert_arr = [];
        this.search();
        this.getİlan();
    }
    search(){
        this.ajaxRequest(this.api_url.ilan ,{},'GET')
            .then(res=> {
                    this.search_btn.ilan_count.text(res.length);
                }
            )

    }



    buildList(res) {
        this.data_arr = res;
        const current_date = new Date();
        this.divs.ilanlar.empty();
        res.map(e => {
            const date = new Date(e.date);
            const Difference_In_Time = current_date.getTime() - date.getTime();
            const Difference_In_Days = (Difference_In_Time / (1000 * 3600 * 24)) < 1
                ? "Dün"
                : `${parseInt(Difference_In_Time / (1000 * 3600 * 24))} gün`;
            const list_element = $(`
                <div class="main_ilan_item row">
                    <div class="main_ilan-item-body">
                        <span >${e.company.name}</span>
                        <span >${e.title}</span>
                        <span >${e.city}</span>
                        <span >${e.type}</span>
                    </div>
            </div>
            `);
            const action_element =
                user_durum === "üye"
                    ?
                    $(`
                        <div class="main_ilan-item-actions">
                            <a id="ilan_detay" class="pointer" data-id="${e.id}" onclick="main_page.openDetailModal(this.dataset.id)"></i> Detay</a>
                            <a class="total_apply pointer" ><i class="fa fa-circle-check"></i> Başvur</a>
                        </div>
                        `)
                    :
                    $(`
                        <div class="item-actions">
                        </div>
                        `)

            action_element.appendTo(list_element);
            list_element.appendTo(this.divs.ilanlar);
        });
    }

    getİlan(){
        this.ajaxRequest(this.api_url.ilan, '', 'GET')
            .then(res => {
                this.buildList(res)
            })
    }

    openDetailModal(id){
        this.ajaxRequest(
            `http://127.0.0.1:8014/api/ilan/?format=json&id=${id}`,
            '',
            'GET'
        )
            .then(res => {
                this.modal.detay.title.html(res[0].title)
                this.modal.detay.company.html(res[0].company.name)
                this.modal.detay.type.html(res[0].type)
                this.modal.detay.city.html(res[0].city)
                this.modal.detay.desc.html(res[0].description)
            })
        this.modal.detay.main.show()
    }

    closeModal(){
        this.modal.detay.main.hide()
    }

    filters(){
        let type = this.inputs.type.val();
        let city = this.inputs.city.val();
        this.ajaxRequest(
            `http://127.0.0.1:8014/api/ilan/?city=${city}&format=json&type=${type}`,
            '',
            'GET'
        )
            .then(res => {
                 this.buildList(res)
            })


        console.log(type, city)

    }
}

let main_page = new Main_Page();