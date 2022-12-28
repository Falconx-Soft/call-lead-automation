// cookie policy
const getCookie = (name) => {
    const value = " " + document.cookie;
    // console.log("value", `==${value}==`);
    const parts = value.split(" " + name + "=");
    return parts.length < 2 ? "cookie not set" : parts.pop().split(";").shift();
};

const setCookie = function (name, value, expiryDays, domain, path, secure) {
    // console.log("Accept fun");
    const exdate = new Date();
    exdate.setHours(
        exdate.getHours() +
        (typeof expiryDays !== "number" ? 365 : expiryDays) * 24
    );
    document.cookie =
        name +
        "=" +
        value +
        ";expires=" +
        exdate.toUTCString() +
        ";path=" +
        (path || "/") +
        (domain ? ";domain=" + domain : "") +
        (secure ? ";secure" : "");
};

const cookieName = "cookiesBanner";
const hasCookie = getCookie(cookieName);
const accept_cookies = document.getElementById("accept-cookies");

// console.log("********", hasCookie);

if (hasCookie == "cookie not set"){
    // console.log("Cookies not accepted");
    $('#exampleModalCenter').modal({
        backdrop: 'static',
        keyboard: false
    });
    $("#exampleModalCenter").modal('show');
}

accept_cookies.addEventListener("click", () => {
    // console.log("Clicked");
    setCookie(cookieName, "accept");
  });