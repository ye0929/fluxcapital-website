(function(){
  var DICT={
    en:{"page.title":"Flux Capital Ltd | 通量资本","hero.title":"Flux Capital Ltd","hero.sub":"通量资本","footer.name":"Flux Capital Ltd · 通量资本","nav.about":"About","nav.business":"Business","nav.contact":"Contact","hero.eyebrow":"Proprietary Trading","hero.lead":"Disciplined, technology-driven trading with our own capital.","hero.cta":"Get in touch","about.title":"About Us","about.body":"Flux Capital Ltd is a privately held company focused on trading financial markets, including digital assets, using its own capital. We combine systematic research, automation and strict risk management to pursue long-term, sustainable results.","biz.title":"Business Scope","biz.c1t":"Proprietary Trading","biz.c1":"We trade exclusively with the company's own capital.","biz.c2t":"Research & Technology","biz.c2":"Quantitative research, backtesting and automated execution.","biz.c3t":"Risk Management","biz.c3":"Defined position limits, stop-losses and capital preservation first.","biz.note":"Flux Capital Ltd does not manage client funds, does not solicit or accept investment from the public, and does not provide investment advice.","contact.title":"Contact","contact.body":"For general enquiries, please email us:","footer.disclaimer":"Disclaimer: The information on this website is for general informational purposes only. It does not constitute an offer or solicitation to buy or sell any securities or financial products, nor investment, legal or tax advice.","footer.rights":"All rights reserved.","404.title":"Page not found","404.body":"The page you are looking for does not exist.","404.back":"Back to home"},
    zh:{"page.title":"通量资本 Flux Capital Ltd","hero.title":"通量资本","hero.sub":"Flux Capital Ltd","footer.name":"通量资本 Flux Capital Ltd","nav.about":"关于我们","nav.business":"业务范围","nav.contact":"联系方式","hero.eyebrow":"自营交易","hero.lead":"以自有资金进行严谨、技术驱动的交易。","hero.cta":"联系我们","about.title":"关于我们","about.body":"通量资本（Flux Capital Ltd）是一家私人持有的公司，专注于使用公司自有资金交易金融市场（包括数字资产）。我们结合系统化研究、自动化执行和严格的风险管理，追求长期、可持续的成果。","biz.title":"业务范围","biz.c1t":"自营交易","biz.c1":"仅使用公司自有资金进行交易。","biz.c2t":"研究与技术","biz.c2":"量化研究、策略回测与自动化执行。","biz.c3t":"风险管理","biz.c3":"明确的仓位限制和止损，资本安全优先。","biz.note":"通量资本（Flux Capital Ltd）不管理客户资金，不向公众募集或接受投资，也不提供投资建议。","contact.title":"联系方式","contact.body":"一般咨询请发送邮件至：","footer.disclaimer":"免责声明：本网站内容仅供一般信息参考，不构成买卖任何证券或金融产品的要约或招揽，也不构成投资、法律或税务建议。","footer.rights":"版权所有。","404.title":"页面未找到","404.body":"您访问的页面不存在。","404.back":"返回首页"}
  };
  var KEY="fluxcapital-lang";
  function store(k,v){try{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v);}catch(e){return null;}}
  function initial(){
    var q=new URLSearchParams(location.search).get("lang");
    if(q==="zh"||q==="en"){store(KEY,q);return q;}
    var s=store(KEY); if(s==="zh"||s==="en")return s;
    return (navigator.language||"en").toLowerCase().indexOf("zh")===0?"zh":"en";
  }
  function apply(lang){
    var d=DICT[lang];
    document.querySelectorAll("[data-i18n]").forEach(function(el){var k=el.getAttribute("data-i18n");if(d[k]!=null)el.textContent=d[k];});
    if(d["page.title"]&&!document.body.hasAttribute("data-no-title"))document.title=d["page.title"];
    document.documentElement.lang=lang==="zh"?"zh-CN":"en";
    var b=document.getElementById("lang-toggle"); if(b)b.textContent=lang==="zh"?"EN":"中文";
    current=lang;
  }
  var current=initial();
  document.addEventListener("DOMContentLoaded",function(){
    apply(current);
    var y=document.getElementById("year"); if(y)y.textContent=new Date().getFullYear();
    var b=document.getElementById("lang-toggle");
    if(b)b.addEventListener("click",function(){var n=current==="zh"?"en":"zh";store(KEY,n);apply(n);});
  });
  if(document.readyState!=="loading")apply(current);
})();
