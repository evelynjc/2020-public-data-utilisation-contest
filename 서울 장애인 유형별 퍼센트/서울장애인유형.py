# readline_all.py
import json
from collections import defaultdict

file_data = defaultdict(lambda: defaultdict(list))
name_list = ["종로구","중구","용산구","성동구","광진구","동대문구","중랑구","성북구","강북구","도봉구","노원구","은평구","서대문구","마포구","양천구","강서구","구로구","금천구","영등포구","동작구","관악구","서초구","강남구","송파구","강동구"]
f = open("seoul.txt", 'r', encoding='UTF8')
idx = 0;
while True:
    line = f.readline()
    if not line: break
    if line.split('\t')[2] == "소계":
            file_data[name_list[idx]]["년도"] = line.split('\t')[0]
            total=""
            file_data[name_list[idx]]["전체"] = temp = line.split('\t')[3]
            for temp_s in temp.split(","):
                total += temp_s

            file_data[name_list[idx]]["지체"] = temp_pd = line.split('\t')[6]
            pd =""            
            for temp_s in temp_pd.split(","):
                pd +=temp_s
            file_data[name_list[idx]]["지체_비율"] = int(pd)/int(total)*100


            file_data[name_list[idx]]["뇌병변"] =temp_bl= line.split('\t')[9]
            bl = ""
            for temp_s in temp_bl.split(","):
                bl +=temp_s

            file_data[name_list[idx]]["뇌병변_비율"] = int(bl)/int(total)*100


            file_data[name_list[idx]]["시각"] =temp_vi=line.split('\t')[12]
            vi = ""
            for temp_s in temp_vi.split(","):
                vi +=temp_s
            file_data[name_list[idx]]["시각_비율"] = int(vi)/int(total)*100


            file_data[name_list[idx]]["청각"] =temp_hi = line.split('\t')[15]
            hi = ""
            for temp_s in temp_hi.split(","):
                hi +=temp_s
            file_data[name_list[idx]]["청각_비율"] = int(hi)/int(total)*100

            
            file_data[name_list[idx]]["언어"] = temp_si = line.split('\t')[18]
            si = ""
            for temp_s in temp_si.split(","):
                si +=temp_s
            file_data[name_list[idx]]["언어_비율"] = int(si)/int(total)*100

            
            file_data[name_list[idx]]["지적장애"] = temp_id = line.split('\t')[21]
            id = ""
            for temp_s in temp_id.split(","):
                id +=temp_s
            file_data[name_list[idx]]["지적장애_비율"] = int(id)/int(total)*100

            
            file_data[name_list[idx]]["자폐"] =temp_ad =line.split('\t')[24]
            ad = ""
            for temp_s in temp_ad.split(","):
                ad +=temp_s
            file_data[name_list[idx]]["자폐_비율"] = int(ad)/int(total)*100

            
            file_data[name_list[idx]]["정신장애"] = temp_md=line.split('\t')[27]
            md = ""
            for temp_s in temp_md.split(","):
                md +=temp_s
            file_data[name_list[idx]]["정신장애_비율"] = int(md)/int(total)*100


            file_data[name_list[idx]]["신장장애"] =temp_kf = line.split('\t')[30]
            kf = ""
            for temp_s in temp_kf.split(","):
                kf +=temp_s
            file_data[name_list[idx]]["신장장애_비율"] = int(kf)/int(total)*100

                
            file_data[name_list[idx]]["심장장애"] = temp_hd = line.split('\t')[33]
            hd=""
            for temp_s in temp_hd.split(","):
                hd +=temp_s
            file_data[name_list[idx]]["심장장애_비율"] = int(hd)/int(total)*100


            file_data[name_list[idx]]["호흡기"] = temp_rd = line.split('\t')[36]
            rd=""
            for temp_s in temp_rd.split(","):
                rd +=temp_s
            file_data[name_list[idx]]["호흡기_비율"] = int(rd)/int(total)*100


            file_data[name_list[idx]]["간"] =temp_ld =  line.split('\t')[39]
            ld=""
            for temp_s in temp_ld.split(","):
                ld +=temp_s
            file_data[name_list[idx]]["간_비율"] = int(ld)/int(total)*100


            file_data[name_list[idx]]["안면"] = temp_fd = line.split('\t')[42]
            fd=""
            for temp_s in temp_fd.split(","):
                fd +=temp_s
            file_data[name_list[idx]]["안면_비율"] = int(fd)/int(total)*100

            
            file_data[name_list[idx]]["장루요루"] = temp_st = line.split('\t')[45]
            st=""
            for temp_s in temp_st.split(","):
                st +=temp_s
            file_data[name_list[idx]]["장루요루_비율"] = int(st)/int(total)*100
            
            file_data[name_list[idx]]["뇌전증"] = temp_e = line.split('\t')[48]
            e=""
            for temp_s in temp_e.split(","):
                e +=temp_s
            file_data[name_list[idx]]["장루요루_비율"] = int(e)/int(total)*100
            
            idx +=1
f.close()
print(json.dumps(file_data,ensure_ascii=False, indent="\t"))
