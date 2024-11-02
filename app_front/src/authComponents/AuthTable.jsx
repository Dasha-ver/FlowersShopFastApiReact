import React, {useState, useEffect} from 'react';
import AuthService from "../services/auth.service";
import {useNavigate} from 'react-router-dom';
import user_pic from '../pictures/user-pic.png'
import auth_basket_pic from '../pictures/auth-basket-pic.png'
import logout_pic from '../pictures/logout-pic.png'

const AuthTable = () => {

    const [token, setToken] = useState(undefined);

    const navigate = useNavigate();

    useEffect(() => {
        const token = AuthService.getToken();

    if (token) {
        setToken(token);
        }
    }, []);

    const logOut = () => {
        AuthService.logout();
    };

    return(
        <div>
        {token ? (
          <table class='auth-table'>
            <td>
              <button class='auth-btn' onClick={() => navigate("/user")}>
                <img className="auth-pic" src={user_pic} alt="auth-pic"/>
              </button>
            </td>
            <td>
              <button class='auth-btn' onClick={() => navigate("/private")}>
                <img className="auth-pic" src={auth_basket_pic} alt="auth-pic"/>
              </button>
            </td>
            <td>
              <a href="/login" onClick={logOut}>
                <img className="auth-pic" src={logout_pic} alt="auth-pic"/>
              </a>
            </td>
          </table>
        ) : (
          <table class='auth-table'>
            <td>
              <button class='auth-btn' onClick={() => navigate("/login")}>
                Войти
              </button>
            </td>

            <td>
              <button class='auth-btn' onClick={() => navigate("/signup")}>
                Регистрация
              </button>
            </td>
          </table>
        )}
      </div>
        )
    }


export default AuthTable;