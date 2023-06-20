let page_main = document.querySelector(".somdPage");
let page_header = document.querySelector(".somdPage_header");
let somdList = document.querySelector(".somdList");
let all_somdList = document.querySelector(".all_somdList");
let option = document.querySelector(".option");
let title = document.querySelector(".mainTitle")
let EmptyForTitle = document.querySelector(".EmptyForTitle")
let Scroll = page_main.scrollTop;
console.log("연결");

page_main.addEventListener('scroll', function(event){
    Scroll  = page_main.scrollTop;
    // console.log(Scroll);
    if(Scroll>160){
        somdList.style.display = "none";
        title.style.display ="none";
        EmptyForTitle.style.height = "50px";
        page_header.appendChild(option);
    }
    if(Scroll < 2){
        somdList.style.display = "block";
        title.style.display ="block";
        EmptyForTitle.style.height = "0px";
        page_main.insertBefore(option,all_somdList);
    }
    //  console.log(option.parentNode);
});
// 


