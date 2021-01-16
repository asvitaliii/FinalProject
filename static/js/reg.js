$(document).ready(function(){
console.log('go')
    let login_valid = false;
    let password_valid = false;
    let password_confirm_valid = false;

    let login_exp = /^[a-zA-Z0-9]{5,15}$/;
    $('#login_field').blur(function(){
        let login_val = $(this).val()
        if (!login_exp.test(login_val)){
            $('#login_err').text('Некорректный логин!');
            login_valid = false
        }else{
            console.log('ajax started')
            $.ajax({
                url: '/ajax_reg',
                data: 'login_field=' + login_val,
                success: function(result){
                    if (result.message_login==='Логин занят!'){
                        $('#login_err').text(result.message_login);
                        login_valid = false
                        console.log('bad login')
                    }else{
                        $('#login_err').text('');
                        login_valid = true
                        console.log('good login')
                    }
                }
            })
            console.log('ajax ended')
        }
        console.log(login_valid)
    })

    $('#login_field').focus(function(){
        $('#login_err').text('');
    })

    $('#password_field').blur(function(){
        let password_val=$(this).val()
        if (password_val.length>7 && password_val.length<16){
            $('#password_err').text('');
            password_valid = true;
        }else{
            $('#password_err').text('Пароль должен быть от 8 до 15 символов!');
            password_valid = false;
        }
    })

    $('#password_field').focus(function(){
        $('#password_err').text('');
    })

    $('#password_confirmation_field').blur(function(){
        let password_confirm_val=$(this).val()
        let password_val=$('#password_field').val()
        if (password_val === password_confirm_val){
            $('#password_confirmation_err').text('');
            password_confirm_valid = true;
        }else{
            $('#password_confirmation_err').text('Пароли должны совпадать!');
            password_confirm_valid = false;
        }
    })

    $('#password_confirmation_field').focus(function(){
        $('#password_confirmation_err').text('');
    })

    $('#submit').click(function(){
        if (login_valid===true && password_valid===true && password_confirm_valid===true){
            $('.form').attr('onsubmit', 'return true');
        }
    })
})

