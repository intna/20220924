from pyecharts import options as opts
from pyecharts.charts.composite_charts import page
from pyecharts.globals import ThemeType, SymbolType
from pyecharts.charts import Pie,Bar,WordCloud,Page,Line,Liquid

#上海大学图书馆数据可视化大屏制作

'''普通柱状图'''
xa1 = ["2013","2014","2015","2016","2017","2018","2019"]
yuyue = ["12465","13546","14822","15487","16597","13654","15469"]
ruguan = ["1782546","1654896","1354662","1678456","1943245","1754623","1945632"]
waijie = ["245059","231246","261235","232546","265481","271549","265412"]
bar =  (Bar()
        .add_xaxis(xa1)
        .add_yaxis('预约',yuyue)
        .add_yaxis('入馆',ruguan)
        .add_yaxis("外借",waijie)
        .set_global_opts(title_opts=opts.TitleOpts(title="2013-2019上海大学图书馆数据对比"))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False)))


'''词云图'''
words = [
    ('图书馆藏书数', 10000),
    ('环境', 4386),
    ('地理位置', 4055),
    ('氛围', 2467),
    ('座椅质量', 2244),
    ('排列规则', 1868),
    ('借书难易程度', 1484),
    ('人流量', 1112),
    ('声誉', 865),
    ('政策', 847),
    ('会员制度', 582),
    ('福利', 555),
    ('优惠券', 432),
    ('开放时间', 420),
    ('座位数', 360),
    ('是否有热水', 270),
    ('安检力度', 210),
    ('采光', 200),  
]
def wordcloud_base() -> WordCloud:
    c = (
        WordCloud()
        .add("", words, word_size_range=[20, 100], shape=SymbolType.ROUND_RECT)
        .set_global_opts(title_opts=opts.TitleOpts(title='企业决策高频词分析图'))
    )
    return c




'''饼图'''
a1 = [('预约数', 76378), ('入馆数', 12498397), ('外借数', 1715143)]
lq_one = 0.96

def one_bin():


    pie = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS))
            .add("数据比例", list(a1))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            .set_global_opts(title_opts=opts.TitleOpts(title='上海大学图书馆数据百分比'),
                             legend_opts=opts.LegendOpts(pos_right="25%"))
    )
    return pie
 
 
'''水滴图'''
liquid = (
        Liquid()
            .add("吴伟彬", [lq_one, lq_one - 0.1])

            .set_global_opts(title_opts=opts.TitleOpts(title="线下入馆比例"))
    )


'''读书种类数量'''
country_num = [('医疗',6),('教育',12),('小说',56),('科普',74),('计算机领域',52),('专业知识',23),('童话',16),('美食',5),('旅游',4),('科技',4),('报刊',3),('其他',16)]

country = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS,height="500px"))
    .add(
        "",
        #[(lable,value),(lable,value),(lable,value)......]
        country_num[0:7],
        radius=["30%", "75%"],
        center=["25%", "50%"],
        rosetype="radius",
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add(
        "",
        country_num[7:],
        radius=["30%", "75%"],
        center=["75%", "50%"],
        rosetype="area",
        label_opts=opts.LabelOpts(is_show=False),
    )
)



'''归还时间变化图'''
xa2 = ["2013","2014","2015","2016","2017","2018","2019"]
score = [1034.2,1168.5,1021.3,1279.6,1428.9,1688.7,1801.3]

bar1 = (Bar()
    .add_xaxis(xa2)
    .add_yaxis("归还时间", score)
    .reversal_axis()
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    .set_global_opts(title_opts=opts.TitleOpts(title="2013-2019图书归还时间对比")))

def line_rental_duration():
    line=(
    Line(init_opts=opts.InitOpts(theme=ThemeType.MACARONS,height="500px"))
    .set_global_opts(

        title_opts=opts.TitleOpts(title='2013-2019图书归还时间对比'),
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(axislabel_opts={"interval":"0"}),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        )
    .add_xaxis(xaxis_data=xa2)
    .add_yaxis(
        series_name="归还时间",
        y_axis=score,
        symbol="emptyCircle",
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),
        )
    )
    return line

'''整合'''
# page = Page(layout=Page.DraggablePageLayout, page_title="上海大学图书馆数据分析")
# page.add(
#     bar,
#     line_rental_duration(),
#     country,
#     one_bin(),
#     liquid,
#     bar1,
#     wordcloud_base()
# )
# page.render('all.html')


Page.save_resize_html("all.html", cfg_file="over.json", dest="over.html")