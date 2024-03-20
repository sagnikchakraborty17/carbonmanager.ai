window.parent.document.getElementById('button-17').addEventListener('click', showPopup);
window.parent.document.getElementById('button-17').addEventListener('click', changeText);
window.parent.document.getElementById('popup').addEventListener('click', hidePopup);

function showPopup() {
    window.parent.document.getElementById('popup').style.display = 'block';
    window.parent.document.getElementById('button-17').style.display = 'none';
};
function hidePopup() {
    window.parent.document.getElementById('popup').style.display = 'none';
    window.parent.document.getElementById('button-17').style.display = 'block';
};
var texts = [
    "Each year, human activities release over 40 billion tCO₂ into the atmosphere.",
    "The production of one kilogram of beef is associated with approximately 26 kgCO₂ emissions.",
    "The transportation sector accounts for nearly 25% of global CO₂ emissions, with the aviation industry being a major contributor.",
    "Deforestation contributes to about 10% of global carbon emissions, releasing stored carbon in trees into the atmosphere",
    "Some carbon offset projects, like reforestation initiatives, can sequester up to 20 tCO₂ per acre over several decades.",
    "Driving an electric vehicle can reduce an individual's carbon footprint by around 50% compared to a conventional gasoline-powered car.",
    "Approximately 3 kgCO₂ is produced when using 1GB of data, and watching an HD-quality movie on Netflix causes approximately 4.5 kgCO₂ emissions.",
	"Globally, buildings are responsible for approximately 36% of total energy use and 39% of CO₂ emissions.",
    "The annual global carbon footprint from the fashion industry is estimated to be around 3.3 billion tons of CO₂.",
    "As of 2021, the average global temperature has increased by approximately 1.2 degrees Celsius compared to pre-industrial levels.",
    "The Amazon rainforest, often referred to as the 'lungs of the Earth,' produces around 20% of the world's oxygen.",
    "In 2019, renewable energy accounted for about 26.2% of global electricity production.",
	"Worldwide, over 90 million barrels of crude oil are consumed each day, contributing to CO₂ emissions.",
    "The global use of coal for electricity generation surpasses 9,000 million metric tons annually.",
    "Approximately 1.3 billion tons of food are wasted globally each year, leading to significant carbon emissions.",
    "The aviation industry is responsible for more than 2% of global CO₂ emissions.",
    "In 2020, global carbon dioxide emissions decreased by around 5.8% due to the COVID-19 pandemic.",
    "The production of one ton of cement releases about 1 ton of CO₂ into the atmosphere.",
    "Over 1.5 billion new smartphones are manufactured each year, contributing to electronic waste and carbon emissions.",
    "The burning of fossil fuels for energy production accounts for over 70% of global greenhouse gas emissions.",
    "Annually, deforestation results in the loss of around 7 million hectares of forest, releasing stored carbon.",
    "The Paris Agreement aims to limit global warming to well below 2 degrees Celsius above pre-industrial levels.",
    "Roughly 25% of the world's population relies on biomass (wood, charcoal) for cooking, contributing to indoor air pollution and carbon emissions.",
    "The ocean absorbs about 30% of the CO₂ released into the atmosphere, leading to ocean acidification.",
    "Every year, over 8 million metric tons of plastic enter the oceans, contributing to marine pollution and environmental harm.",
    "The construction industry is responsible for nearly 40% of global energy-related CO₂ emissions.",
    "The average American generates over 16 metric tons of carbon dioxide emissions annually."
];

function changeText() {
    var randomIndex = Math.floor(Math.random() * texts.length);
    var newText = texts[randomIndex];

    window.parent.document.getElementById('popupText').innerHTML = newText;
};

if (!window.parent.document.querySelector('[class^=icon2]')) {
    var newDiv = document.createElement('span');
            
    newDiv.className  = 'icon2';

    var button = window.parent.document.querySelector('div[id^=tabs-bui][id$=-tabpanel-4] > div > div > div > div > div > div > div> div > div > div > button[kind = "secondary"] > div');

    button.appendChild(newDiv);
};

if (!window.parent.document.querySelector('[class^=icon3]')) {
    var newDiv2 = document.createElement('span');
            
    newDiv2.className  = 'icon3';

    var button2 = window.parent.document.querySelector('div[id^=tabs-bui][id$=-tabpanel-2] > div > div > div > div > div > div > div> div > div > div > button[kind = "secondary"] > div');

    button2.appendChild(newDiv2);
};
                        
function checkScreenWidth() {
  var screenWidth = window.innerWidth || window.parent.document.documentElement.clientWidth || window.parent.document.body.clientWidth;

  if (screenWidth <= 600) {
            window.parent.document.getElementById('project-copyright').style.display = 'none';
			Array.from(window.parent.document.querySelectorAll('button[data-baseweb="tab"] > div > p')).forEach(button => button.style.fontSize = '10px');
  } else {
            window.parent.document.getElementById('project-copyright').style.display = 'block';
  }
}

window.onload = checkScreenWidth;
window.onresize = checkScreenWidth;

(()=>{const e="bp-web-widget",t={};function n(t){return t?`${t}-container`:e}function o(e){return e||"bp-widget"}function i(e,t,n={}){const o=document.createElement(e);Object.entries(n).forEach((([e,t])=>o[e]=t));const i=document.querySelector(t);if(!i)throw new Error(`No element correspond to ${t}`);return i.appendChild(o),o}function r(e,t){const n=`bp-chat-key-${t.clientId}`;let i=localStorage.getItem(n);i||(i=function(e){const t="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";let n="";for(let o=0;o<e;o++)n+=t.charAt(Math.floor(Math.random()*t.length));return n}(32),localStorage.setItem(n,i));const r=encodeURIComponent(JSON.stringify({config:Object.assign(Object.assign({},t),{encryptionKey:i})})),a=encodeURIComponent(t.botConversationDescription||t.botName||"Chatbot"),c=e+"/index.html?options="+r;return`<iframe id="${o(t.chatId)}" title="${a}" frameborder="0" src="${c}" class="bp-widget-web"/>`}function a(e,t){return new Proxy(t,{get:(t,n)=>t[n]?t[n]:"iframeWindow"===n?()=>{console.warn(`No webchat with id ${e} has been initialized. \n Please use window.botpressWebChat.init first.`)}:"eventListener"===n?{handler:()=>{},types:[]}:void 0,set:(e,t,n)=>(e[t]=n,!0)})}function c(n){return t[n=n||e]}function s(e,t){return document.querySelector(`#${e} #${t}`)}window.addEventListener("message",(function({data:e}){var t,i,r;if(!function(e){return e&&"string"==typeof e.type&&"string"==typeof e.chatId}(e))return;if("UI.RESIZE"===e.type){const t="number"==typeof e.value?e.value+"px":e.value;s(n(e.chatId),o(e.chatId)).style.width=t}if("UI.SET-CLASS"===e.type){s(n(e.chatId),o(e.chatId)).setAttribute("class",e.value)}const a=c(e.chatId);a&&(null===(t=a.eventListener.topics)||void 0===t?void 0:t.some((t=>"*"===t||t===e.type)))&&(null===(r=(i=a.eventListener).handler)||void 0===r||r.call(i,e))})),window.botpressWebChat={init:function(c,d){d=d||"body",c.chatId=c.chatId||e;const f=c.hostUrl||"";i("link","head",{rel:"stylesheet",href:`${f}/inject.css`});const l=r(f,c),u=n(c.chatId),h=o(c.chatId);i("div",d,{id:u,innerHTML:l});const p={iframeWindow:s(u,h).contentWindow};t[c.chatId]?Object.assign(t[c.chatId],p):t[c.chatId]=a(c.chatId,p)},configure:function(e,t){c(t).iframeWindow.postMessage({action:"configure",payload:e},"*")},sendEvent:function(e,t){c(t).iframeWindow.postMessage({action:"event",payload:e},"*")},mergeConfig:function(e,t){c(t).iframeWindow.postMessage({action:"mergeConfig",payload:e},"*")},sendPayload:function(e,t){c(t).iframeWindow.postMessage({action:"sendPayload",payload:e},"*")},onEvent:function(n,o=[],i){if("function"!=typeof n)throw new Error("EventHandler is not a function, please provide a function");if(!Array.isArray(o))throw new Error("Topics should be an array of supported event types");const r={eventListener:{handler:n,topics:o}};t[i=i||e]?Object.assign(t[i],r):t[i]=a(i,r)}}})();
//# sourceMappingURL=inject.js.map

window.botpressWebChat.init({
    "composerPlaceholder": "Chat with CarbonGPT",
    "botConversationDescription": "This is the bot for the Carbon Manager project. ",
    "botId": "c80ccde7-2db0-4ca9-99b0-14c91448ee4e",
    "hostUrl": "https://cdn.botpress.cloud/webchat/v1",
    "messagingUrl": "https://messaging.botpress.cloud",
    "clientId": "c80ccde7-2db0-4ca9-99b0-14c91448ee4e",
    "webhookId": "756ed999-5e57-4054-9f7a-9c23a7c9b8d1",
    "lazySocket": true,
    "themeName": "prism",
    "botName": "CarbonGPT",
    "avatarUrl": "https://cdn.leonardo.ai/users/434a484d-c18d-47a0-9d78-7c1cfca70039/generations/0e5b096c-fa85-4d78-b42a-6fb37e24935e/Default_woman_dancing_in_the_black_hole_splashing_ripples_on_b_0.jpg?w=512",
    "frontendVersion": "v1",
    "useSessionStorage": true,
    "enableConversationDeletion": true,
    "theme": "prism",
    "themeColor": "#2563eb"
});
