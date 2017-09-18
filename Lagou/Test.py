from bs4 import BeautifulSoup
html='''
<li class="con_list_item default_list" data-index="2" data-positionid="3601090" data-salary="2k-4k" data-company="启迪金控" data-positionname="爬虫工程师（实习生）" data-companyid="162510" data-hrid="6653735">
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/3601090.html" target="_blank" data-index="2" data-lg-tj-id="8E00" data-lg-tj-no="
                    0103
                " data-lg-tj-cid="3601090" data-lg-tj-abt="dm-csearch-useUserInterest|0">
                        <h3 style="max-width: 180px;">爬虫工程师（实习生）</h3>
                                    <span class="add">[<em>中关村</em>]</span>

                    </a>
                    <span class="format-time">2017-09-13</span>
'''

soup=BeautifulSoup(html,'lxml')
a=soup.find(name='li',class_='con_list_item default_list')
date_soup=BeautifulSoup(str(a),'lxml')
date=date_soup.find(name='span',class_='format-time').text
print(date)