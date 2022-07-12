class Ilanlarim extends App{
    constructor() {
        super();
        this.data_arr = null;
        this.button = {
            ilan_panel : $('#ilan-panel'),

        }
        this.modal = {
            create: {
                main : $('#create_ilan_modal'),
                title: $('#create_title'),
                type: $('#create_working_type'),
                city: $('#create_city'),
                company: $('#create_company_select'),
                desc : $('#create_desc'),
            }

        }
        this.IlanGetir()
    }

    showCreateModal(){
        this.ajaxRequest(
            this.api_url.company,
            '',
            'GET'
        )
            .then(res=>{
                res.map(i => {

                    this.modal.create.company.append($('<option>', { value : i.id })
                        .text(i.name));
                })
            })
        this.modal.create.main.show();
    }

    IlanGetir(){
        this.ajaxRequest(
            this.api_url.ilan_yayinlayan_filter,
            '',
            'GET'
        )
            .then(res =>{
                this.data_arr = res;
                const current_date = new Date();
                res.map(i => {
                    const date = new Date(i.date);
                    const Difference_In_Time = current_date.getTime() - date.getTime();
                    const Difference_In_Days = (Difference_In_Time / (1000 * 3600 * 24)) < 1
                        ? "Dün"
                        : `${parseInt(Difference_In_Time / (1000 * 3600 * 24))} gün`;
                    this.button.ilan_panel.append(`
                    
                    <div class="ilan-item">
                        <div class="ilan-item-body">
                            <span >${i.title}</span>
                            <span >${i.city}</span>
                            <span >${i.type}</span>
                            <span >${Difference_In_Days}</span>
                        </div>
                        <div class="ilan-item-actions">
                            <a class="ilan_detail" data-id="${i.id}" ><i class="fa fa-circle-info"></i> Detay</a>
                            <a class="total_apply" data-id="${i.id}" ><i class="fa fa-circle-check"></i> 1 başvuru</a>
                        </div>
                     </div>
                    `)
                })
            })
    }

    ilanEkle(){
        const date = new Date();

        this.ajaxRequest(
            this.api_url.create_ilan, {
                yayinlayan: user_id,
                company: this.modal.create.company.val(),
                date: `${date.getFullYear()}-${date.getDay()}-${date.getDate()}`,
                type: this.modal.create.type.val(),
                city: this.modal.create.city.val(),
                title: this.modal.create.title.val(),
                description: this.modal.create.desc.val(),
            }, 'POST'
        )
            .then(res => console.log(res))
    }



}

let ilanlarim_page = new Ilanlarim()