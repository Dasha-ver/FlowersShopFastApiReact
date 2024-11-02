import React, { useState, useEffect } from "react";
import Resource from "../services/resource.service";
import AuthService from "../services/auth.service";
import { useNavigate } from "react-router-dom";

const Private = () => {
  const [privateInfo, setPrivateInfo] = useState("");

  const navigate = useNavigate();

  useEffect(() => {
    Resource.getPrivateResource().then(
      (response) => {
        console.log("Private page", response.data)
        setPrivateInfo(response.data.detail);
      },
      (error) => {
        console.log("Private page", error.response);
        // Invalid token
        if (error.response && error.response.status === 403) {
          AuthService.logout();
          navigate("/login");
          window.location.reload();
        }
      }
    );
  }, []);

  return (
    <div>
      <h3>{privateInfo}</h3>
    </div>
  );
};

export default Private;