from PIL import Image



#standard(stats)
stats = ["player","nationality","position","squad","age","birth_year","games","games_starts","minutes","goals","assists","pens_made","pens_att","cards_yellow","cards_red","goals_per90","assists_per90","goals_assists_per90","goals_pens_per90","goals_assists_pens_per90","xg","npxg","xa","xg_per90","xa_per90","xg_xa_per90","npxg_per90","npxg_xa_per90"]
stats3 = ["players_used","possession","games","games_starts","minutes","goals","assists","pens_made","pens_att","cards_yellow","cards_red","goals_per90","assists_per90","goals_assists_per90","goals_pens_per90","goals_assists_pens_per90","xg","npxg","xa","xg_per90","xa_per90","xg_xa_per90","npxg_per90","npxg_xa_per90"] 
#goalkeeping(keepers)
keepers = ["player","nationality","position","squad","age","birth_year","games_gk","games_starts_gk","minutes_gk","goals_against_gk","goals_against_per90_gk","shots_on_target_against","saves","save_pct","wins_gk","draws_gk","losses_gk","clean_sheets","clean_sheets_pct","pens_att_gk","pens_allowed","pens_saved","pens_missed_gk"]
keepers3 = ["players_used","games_gk","games_starts_gk","minutes_gk","goals_against_gk","goals_against_per90_gk","shots_on_target_against","saves","save_pct","wins_gk","draws_gk","losses_gk","clean_sheets","clean_sheets_pct","pens_att_gk","pens_allowed","pens_saved","pens_missed_gk"]
#advance goalkeeping(keepersadv)
keepersadv = ["player","nationality","position","squad","age","birth_year","minutes_90s","goals_against_gk","pens_allowed","free_kick_goals_against_gk","corner_kick_goals_against_gk","own_goals_against_gk","psxg_gk","psnpxg_per_shot_on_target_against","psxg_net_gk","psxg_net_per90_gk","passes_completed_launched_gk","passes_launched_gk","passes_pct_launched_gk","passes_gk","passes_throws_gk","pct_passes_launched_gk","passes_length_avg_gk","goal_kicks","pct_goal_kicks_launched","goal_kick_length_avg","crosses_gk","crosses_stopped_gk","crosses_stopped_pct_gk","def_actions_outside_pen_area_gk","def_actions_outside_pen_area_per90_gk","avg_distance_def_actions_gk"]
keepersadv2 = ["minutes_90s","goals_against_gk","pens_allowed","free_kick_goals_against_gk","corner_kick_goals_against_gk","own_goals_against_gk","psxg_gk","psnpxg_per_shot_on_target_against","psxg_net_gk","psxg_net_per90_gk","passes_completed_launched_gk","passes_launched_gk","passes_pct_launched_gk","passes_gk","passes_throws_gk","pct_passes_launched_gk","passes_length_avg_gk","goal_kicks","pct_goal_kicks_launched","goal_kick_length_avg","crosses_gk","crosses_stopped_gk","crosses_stopped_pct_gk","def_actions_outside_pen_area_gk","def_actions_outside_pen_area_per90_gk","avg_distance_def_actions_gk"]

#shooting(shooting)

shooting = ["player","nationality","position","squad","age","birth_year","minutes_90s","goals","pens_made","pens_att","shots_total","shots_on_target","shots_free_kicks","shots_on_target_pct","shots_total_per90","shots_on_target_per90","goals_per_shot","goals_per_shot_on_target","xg","npxg","npxg_per_shot","xg_net","npxg_net"]
shooting2 = ["minutes_90s","goals","pens_made","pens_att","shots_total","shots_on_target","shots_free_kicks","shots_on_target_pct","shots_total_per90","shots_on_target_per90","goals_per_shot","goals_per_shot_on_target","xg","npxg","npxg_per_shot","xg_net","npxg_net"]
shooting3 = ["goals","pens_made","pens_att","shots_total","shots_on_target","shots_free_kicks","shots_on_target_pct","shots_total_per90","shots_on_target_per90","goals_per_shot","goals_per_shot_on_target","xg","npxg","npxg_per_shot","xg_net","npxg_net"]
#passing(passing)
passing = ["player","nationality","position","squad","age","birth_year","minutes_90s","passes_completed","passes","passes_pct","passes_total_distance","passes_progressive_distance","passes_completed_short","passes_short","passes_pct_short","passes_completed_medium","passes_medium","passes_pct_medium","passes_completed_long","passes_long","passes_pct_long","assists","xa","xa_net","assisted_shots","passes_into_final_third","passes_into_penalty_area","crosses_into_penalty_area","progressive_passes"]
passing2 = ["minutes_90s","passes_completed","passes","passes_pct","passes_total_distance","passes_progressive_distance","passes_completed_short","passes_short","passes_pct_short","passes_completed_medium","passes_medium","passes_pct_medium","passes_completed_long","passes_long","passes_pct_long","assists","xa","xa_net","assisted_shots","passes_into_final_third","passes_into_penalty_area","crosses_into_penalty_area","progressive_passes"]
#passtypes(passing_types)
passing_types = ["player","nationality","position","squad","age","birth_year","minutes_90s","passes","passes_live","passes_dead","passes_free_kicks","through_balls","passes_pressure","passes_switches","crosses","corner_kicks","corner_kicks_in","corner_kicks_out","corner_kicks_straight","passes_ground","passes_low","passes_high","passes_left_foot","passes_right_foot","passes_head","throw_ins","passes_other_body","passes_completed","passes_offsides","passes_oob","passes_intercepted","passes_blocked"]
passing_types2 = ["passes","passes_live","passes_dead","passes_free_kicks","through_balls","passes_pressure","passes_switches","crosses","corner_kicks","corner_kicks_in","corner_kicks_out","corner_kicks_straight","passes_ground","passes_low","passes_high","passes_left_foot","passes_right_foot","passes_head","throw_ins","passes_other_body","passes_completed","passes_offsides","passes_oob","passes_intercepted","passes_blocked"]
#goal and shot creation(gca)
gca = ["player","nationality","position","squad","age","birth_year","minutes_90s","sca","sca_per90","sca_passes_live","sca_passes_dead","sca_dribbles","sca_shots","sca_fouled","gca","gca_per90","gca_passes_live","gca_passes_dead","gca_dribbles","gca_shots","gca_fouled","gca_og_for"]
gca2 = ["sca","sca_per90","sca_passes_live","sca_passes_dead","sca_dribbles","sca_shots","sca_fouled","gca","gca_per90","gca_passes_live","gca_passes_dead","gca_dribbles","gca_shots","gca_fouled","gca_og_for"]
#defensive actions(defense)
defense = ["player","nationality","position","squad","age","birth_year","minutes_90s","tackles","tackles_won","tackles_def_3rd","tackles_mid_3rd","tackles_att_3rd","dribble_tackles","dribbles_vs","dribble_tackles_pct","dribbled_past","pressures","pressure_regains","pressure_regain_pct","pressures_def_3rd","pressures_mid_3rd","pressures_att_3rd","blocks","blocked_shots","blocked_shots_saves","blocked_passes","interceptions","clearances","errors"]
defense2 = ["tackles","tackles_won","tackles_def_3rd","tackles_mid_3rd","tackles_att_3rd","dribble_tackles","dribbles_vs","dribble_tackles_pct","dribbled_past","pressures","pressure_regains","pressure_regain_pct","pressures_def_3rd","pressures_mid_3rd","pressures_att_3rd","blocks","blocked_shots","blocked_shots_saves","blocked_passes","interceptions","clearances","errors"]
#possession(possession)
possession = ["player","nationality","position","squad","age","birth_year","minutes_90s","touches","touches_def_pen_area","touches_def_3rd","touches_mid_3rd","touches_att_3rd","touches_att_pen_area","touches_live_ball","dribbles_completed","dribbles","dribbles_completed_pct","players_dribbled_past","nutmegs","carries","carry_distance","carry_progressive_distance","progressive_carries","carries_into_final_third","carries_into_penalty_area","pass_targets","passes_received","passes_received_pct","miscontrols","dispossessed"]
possession2 = ["touches","touches_def_pen_area","touches_def_3rd","touches_mid_3rd","touches_att_3rd","touches_att_pen_area","touches_live_ball","dribbles_completed","dribbles","dribbles_completed_pct","players_dribbled_past","nutmegs","carries","carry_distance","carry_progressive_distance","progressive_carries","carries_into_final_third","carries_into_penalty_area","pass_targets","passes_received","passes_received_pct","miscontrols","dispossessed"]
#playingtime(playingtime)
playingtime = ["player","nationality","position","squad","age","birth_year","minutes_90s","games","minutes","minutes_per_game","minutes_pct","games_starts","minutes_per_start","games_subs","minutes_per_sub","unused_subs","points_per_match","on_goals_for","on_goals_against","plus_minus","plus_minus_per90","plus_minus_wowy","on_xg_for","on_xg_against","xg_plus_minus","xg_plus_minus_per90","xg_plus_minus_wowy"]
playingtime2 = ["games","minutes","minutes_per_game","minutes_pct","games_starts","minutes_per_start","games_subs","minutes_per_sub","unused_subs","points_per_match","on_goals_for","on_goals_against","plus_minus","plus_minus_per90","plus_minus_wowy","on_xg_for","on_xg_against","xg_plus_minus","xg_plus_minus_per90","xg_plus_minus_wowy"]
#miscallaneous(misc)
misc = ["player","nationality","position","squad","age","birth_year","minutes_90s","cards_yellow","cards_red","cards_yellow_red","fouls","fouled","offsides","crosses","interceptions","tackles_won","pens_won","pens_conceded","own_goals","ball_recoveries","aerials_won","aerials_lost","aerials_won_pct"]
misc2 = ["cards_yellow","cards_red","cards_yellow_red","fouls","fouled","offsides","crosses","interceptions","tackles_won","pens_won","pens_conceded","own_goals","ball_recoveries","aerials_won","aerials_lost","aerials_won_pct"]


import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import sys, getopt
import csv
import matplotlib.pyplot as plt
from soccerplots.radar_chart import Radar
from PIL import Image


#Functions to get the data in a dataframe using BeautifulSoup
def get_tables(url):
    res = requests.get(url)
    ## The next two lines get around the issue with comments breaking the parsing.
    comm = re.compile("<!--|-->")
    soup = BeautifulSoup(comm.sub("",res.text),'lxml')
    all_tables = soup.findAll("tbody")
    team_table = all_tables[0]
    player_table = all_tables[2]
    return player_table, team_table

def get_frame(features, player_table):
    pre_df_player = dict()
    features_wanted_player = features
    rows_player = player_table.find_all('tr')
    for row in rows_player:
        if(row.find('th',{"scope":"row"}) != None):

            for f in features_wanted_player:
                try:
                    cell = row.find("td",{"data-stat": f})
                    a = cell.text.strip().encode()
                    text=a.decode("utf-8")
                    if(text == ''):
                        text = '0'
                    if((f!='player')&(f!='nationality')&(f!='position')&(f!='squad')&(f!='age')&(f!='birth_year')):
                        text = float(text.replace(',',''))
                    if f in pre_df_player:
                        pre_df_player[f].append(text)
                        
                    else:
                        pre_df_player[f] = [text]
                except:
                    print("fail")
    df_player = pd.DataFrame.from_dict(pre_df_player)
    return df_player

def get_frame_team(features, team_table):
    pre_df_squad = dict()
    #Note: features does not contain squad name, it requires special treatment
    features_wanted_squad = features
    rows_squad = team_table.find_all('tr')
    for row in rows_squad:
        if(row.find('th',{"scope":"row"}) != None):
            name = row.find('th',{"data-stat":"squad"}).text.strip().encode().decode("utf-8")
            if 'squad' in pre_df_squad:
                pre_df_squad['squad'].append(name)
            else:
                pre_df_squad['squad'] = [name]
            for f in features_wanted_squad:
                cell = row.find("td",{"data-stat": f})
                a = cell.text.strip().encode()
                text=a.decode("utf-8")
                if(text == ''):
                    text = '0'
                if((f!='player')&(f!='nationality')&(f!='position')&(f!='squad')&(f!='age')&(f!='birth_year')):
                    text = float(text.replace(',',''))
                if f in pre_df_squad:
                    pre_df_squad[f].append(text)
                else:
                    pre_df_squad[f] = [text]
    df_squad = pd.DataFrame.from_dict(pre_df_squad)
    return df_squad

def frame_for_category(category,top,end,features):
    url = (top + category + end)
    player_table, team_table = get_tables(url)
    df_player = get_frame(features, player_table)
    return df_player

def frame_for_category_team(category,top,end,features):
    url = (top + category + end)
    player_table, team_table = get_tables(url)
    df_team = get_frame_team(features, team_table)
    return df_team

#Function to get the player data for outfield player, includes all categories - standard stats, shooting
#passing, passing types, goal and shot creation, defensive actions, possession, and miscallaneous

#Search for this.

def get_cb_data(top, end):
    df1 = frame_for_category('stats',top,end,stats)
    #df2 = frame_for_category('shooting',top,end,shooting2)
    df3 = frame_for_category('passing',top,end,passing2)
    #df4 = frame_for_category('passing_types',top,end,passing_types2)
    #df5 = frame_for_category('gca',top,end,gca2)
    df6 = frame_for_category('defense',top,end,defense2)
    #df7 = frame_for_category('possession',top,end,possession2)
    df8 = frame_for_category('misc',top,end,misc2)
    #df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], axis=1)
    df = pd.concat([df1,df3, df6, df8], axis=1)

    df = df.loc[:,~df.columns.duplicated()]
    return df

def get_fullback_data(top, end):
    df1 = frame_for_category('stats',top,end,stats)
    #df2 = frame_for_category('shooting',top,end,shooting2)
    df3 = frame_for_category('passing',top,end,passing2)
    #df4 = frame_for_category('passing_types',top,end,passing_types2)
    #df5 = frame_for_category('gca',top,end,gca2)
    df6 = frame_for_category('defense',top,end,defense2)
    df7 = frame_for_category('possession',top,end,possession2)
    df8 = frame_for_category('misc',top,end,misc2)
    #df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], axis=1)
    df = pd.concat([df1,df3, df6,df7,df8], axis=1)
    df = df.loc[:,~df.columns.duplicated()]
    return df

def get_cm_data(top, end):
    df1 = frame_for_category('stats',top,end,stats)
    #df2 = frame_for_category('shooting',top,end,shooting2)
    df3 = frame_for_category('passing',top,end,passing2)
    #df4 = frame_for_category('passing_types',top,end,passing_types2)
    #df5 = frame_for_category('gca',top,end,gca2)
    df6 = frame_for_category('defense',top,end,defense2)
    df7 = frame_for_category('possession',top,end,possession2)
    df8 = frame_for_category('misc',top,end,misc2)
    #df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], axis=1)
    df = pd.concat([df1, df3, df6, df7, df8], axis=1)
    df = df.loc[:,~df.columns.duplicated()]
    return df

def get_cam_data(top, end):
    df1 = frame_for_category('stats',top,end,stats)
    df2 = frame_for_category('shooting',top,end,shooting2)
    df3 = frame_for_category('passing',top,end,passing2)
    #df4 = frame_for_category('passing_types',top,end,passing_types2)
    #df5 = frame_for_category('gca',top,end,gca2)
    df6 = frame_for_category('defense',top,end,defense2)
    df7 = frame_for_category('possession',top,end,possession2)
    df8 = frame_for_category('misc',top,end,misc2)
    #df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], axis=1)
    df = pd.concat([df1, df2, df3, df6, df7, df8], axis=1)
    df = df.loc[:,~df.columns.duplicated()]
    return df

def get_cf_data(top, end):
    df1 = frame_for_category('stats',top,end,stats)
    df2 = frame_for_category('shooting',top,end,shooting2)
    #df3 = frame_for_category('passing',top,end,passing2)
    #df4 = frame_for_category('passing_types',top,end,passing_types2)
    #df5 = frame_for_category('gca',top,end,gca2)
    df6 = frame_for_category('defense',top,end,defense2)
    df7 = frame_for_category('possession',top,end,possession2)
    df8 = frame_for_category('misc',top,end,misc2)
    #df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], axis=1)
    df = pd.concat([df1, df2,df6, df7, df8], axis=1)

    df = df.loc[:,~df.columns.duplicated()]
    return df








#Function to get keeping and advance goalkeeping data
def get_keeper_data(top,end):
    df1 = frame_for_category('keepers',top,end,keepers)
    df2 = frame_for_category('keepersadv',top,end,keepersadv2)
    df = pd.concat([df1, df2], axis=1)
    df = df.loc[:,~df.columns.duplicated()]
    return df

    #Function to get team-wise data accross all categories as mentioned above
def get_team_data(top,end):

    # With a if-statement the user could use if they want attacking stats or defensive stats. 
    df1 = frame_for_category_team('stats',top,end,stats3)
    df2 = frame_for_category_team('keepers',top,end,keepers3)
    df3 = frame_for_category_team('keepersadv',top,end,keepersadv2)
    df4 = frame_for_category_team('shooting',top,end,shooting3)
    df5 = frame_for_category_team('passing',top,end,passing2)
    df6 = frame_for_category_team('passing_types',top,end,passing_types2)
    df7 = frame_for_category_team('gca',top,end,gca2)
    df8 = frame_for_category_team('defense',top,end,defense2)
    df9 = frame_for_category_team('possession',top,end,possession2)
    df10 = frame_for_category_team('misc',top,end,misc2)
    df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10], axis=1)
    df = df.loc[:,~df.columns.duplicated()]
    return df


#This cell is to get the outfield player data for any competition

#Go to the 'Standard stats' page of the league
#For Premier League 2019/20, the link is this: https://fbref.com/en/comps/9/stats/Premier-League-Stats
#Remove the 'stats', and pass the first and third part of the link as parameters like below


def get_player(player1,player2, compareData):
    print(compareData)

### Make this a function, depending on name search, change name.
    if compareData == "CB":
        df_outfield = get_cb_data('https://fbref.com/en/comps/9/','/Premier-League-Stats')


        df_outfield = df_outfield[(df_outfield['player']==player1)  | (df_outfield['player']==player2)].reset_index()
        for x in range(len(df_outfield['player'])):
            if df_outfield['player'][x] == player1:
                squadPlayer1 = df_outfield['squad'].iloc[x]
                a_minutes90s = df_outfield['minutes_90s'][x]

            if df_outfield['player'][x] == player2:
                squadPlayer2 = df_outfield['squad'].iloc[x]
                b_minutes90s = df_outfield['minutes_90s'][x]

        df_outfield = df_outfield.drop(['index','games','games_starts','minutes','goals','assists','pens_made','pens_att','cards_yellow','cards_red','goals_per90','assists_per90','goals_assists_per90','goals_pens_per90','goals_assists_pens_per90','xg','npxg','xa','xg_per90','xa_per90','xg_xa_per90','npxg_per90','npxg_xa_per90','nationality','position','squad','age','birth_year','minutes_90s','tackles','tackles_def_3rd','tackles_mid_3rd','tackles_att_3rd','dribble_tackles','dribbles_vs','dribble_tackles_pct','dribbled_past','pressure_regains','pressure_regain_pct','pressures_def_3rd','pressures_mid_3rd','pressures_att_3rd','blocked_shots','blocked_shots_saves','blocked_passes','interceptions','errors', 'passes_completed','passes','passes_total_distance','passes_progressive_distance','passes_completed_short','passes_short','passes_pct_short','passes_completed_medium','passes_medium','passes_pct_medium','passes_long','passes_pct_long','assists','xa','xa_net','assisted_shots','passes_into_final_third','passes_into_penalty_area','crosses_into_penalty_area', 'cards_yellow','cards_red','cards_yellow_red','fouled','offsides','crosses','interceptions','tackles_won','pens_won','pens_conceded','own_goals','ball_recoveries','aerials_lost','passes_pct', 'aerials_won_pct'],axis=1, errors='ignore')



    if compareData == "CF":
        df_outfield = get_cf_data('https://fbref.com/en/comps/9/','/Premier-League-Stats')


        df_outfield = df_outfield[(df_outfield['player']==player1)  | (df_outfield['player']==player2)].reset_index()
        for x in range(len(df_outfield['player'])):
            if df_outfield['player'][x] == player1:
                squadPlayer1 = df_outfield['squad'].iloc[x]
                a_minutes90s = df_outfield['minutes_90s'][x]

            if df_outfield['player'][x] == player2:
                squadPlayer2 = df_outfield['squad'].iloc[x]
                b_minutes90s = df_outfield['minutes_90s'][x]

        df_outfield = df_outfield.drop(['index','nationality','minutes_90s','position','squad','age','birth_year','goals','pens_made','pens_att','shots_total_per90’,’shots_on_target','shots_free_kicks','shots_on_target_pct','shots_on_target_per90','goals_per_shot','goals_per_shot_on_target','xg_per90','npxg','xg_net','npxg_net', 'xa_per90', 'xg_xa_per90', 'shots_total_per90', 'npxg_per_shot', 'games','games_starts','minutes','goals','assists','pens_made','pens_att','cards_yellow','cards_red','goals_per90','assists_per90','goals_assists_per90','goals_pens_per90','goals_assists_pens_per90','npxg','xa_’per90,’xg_xa_per90','npxg_per90','npxg_xa_per90','touches','touches_def_pen_area','touches_def_3rd','touches_mid_3rd','touches_att_3rd','touches_live_ball','dribbles','dribbles_completed_pct','players_dribbled_past','nutmegs','carries','carry_distance','carry_progressive_distance','progressive_carries','carries_into_final_third','carries_into_penalty_area','pass_targets','passes_received','passes_received_pct','miscontrols','dispossessed', 'nationality','position','squad','age','birth_year','cards_yellow','cards_red','cards_yellow_red','fouls','fouled','offsides','crosses','interceptions','tackles_won','pens_won','pens_conceded','own_goals','ball_recoveries','aerials_lost','aerials_won_pct', 'tackles','tackles_won','tackles_def_3rd','tackles_mid_3rd','tackles_att_3rd','dribble_tackles','dribbles_vs','dribble_tackles_pct','dribbled_past','pressure_regain_pct','pressures_def_3rd','pressures_mid_3rd','pressures_att_3rd','blocks','blocked_shots','blocked_shots_saves','blocked_passes','interceptions','clearances','errors'],axis=1, errors='ignore')

    if compareData == "CAM":
        print("hallå?")
        df_outfield = get_cam_data('https://fbref.com/en/comps/9/','/Premier-League-Stats')

        df_outfield = df_outfield[(df_outfield['player']==player1)  | (df_outfield['player']==player2)].reset_index()
    

        for x in range(len(df_outfield['player'])):
            if df_outfield['player'][x] == player1:
                squadPlayer1 = df_outfield['squad'].iloc[x]
                a_minutes90s = df_outfield['minutes_90s'][x]

            if df_outfield['player'][x] == player2:
                squadPlayer2 = df_outfield['squad'].iloc[x]
                b_minutes90s = df_outfield['minutes_90s'][x]


        df_outfield = df_outfield.drop(['index','nationality','position','npxg_per_shot','squad','age','birth_year','games','games_starts','minutes','goals','assists','pens_made','pens_att','cards_yellow','cards_red','goals_per90','assists_per90','goals_assists_per90','goals_pens_per90','goals_assists_pens_per90','xg_per90','npxg','xa_per90', 'xg_xa_per90','npxg_per90','npxg_xa_per90','minutes_90s','goals','pens_made','pens_att','shots_total_per90','shots_on_target','shots_free_kicks','shots_on_target_pct','shots_on_target_per90','goals_per_shot','goals_per_shot_on_target','npxg','xg_net','npxg_net','touches','touches_def_pen_area','touches_def_3rd','touches_mid_3rd','touches_att_3rd','touches_live_ball','dribbles_completed','dribbles','dribbles_completed_pct','players_dribbled_past','nutmegs','carries','carry_distance','carry_progressive_distance','progressive_carries','carries_into_final_third','carries_into_penalty_area','pass_targets','passes_received','passes_received_pct','miscontrols', 'dispossessed’,’npxg_per_shot', 'passes_pct', 'passes_completed','passes','passes_total_distance','passes_progressive_distance','passes_completed_short','passes_short','passes_pct_short','passes_completed_medium','passes_medium','passes_pct_medium','passes_completed_long','passes_long','passes_pct_long','assists','xa_net','passes_into_final_third','passes_into_penalty_area','progressive_passes','cards_yellow','cards_red','cards_yellow_red','fouls','offsides','crosses','interceptions','tackles_won','pens_won','pens_conceded','own_goals','ball_recoveries','aerials_won','aerials_lost','aerials_won_pct','touches','touches_def_pen_area','touches_def_3rd','touches_mid_3rd','touches_att_3rd','touches_live_ball','dribbles_completed','dribbles','players_dribbled_past','nutmegs','carries','carry_distance','carry_progressive_distance','progressive_carries','carries_into_final_third','carries_into_penalty_area','pass_targets','passes_received','passes_received_pct','miscontrols','dispossessed','tackles','tackles_won','tackles_def_3rd','tackles_mid_3rd','tackles_att_3rd','dribble_tackles','dribbles_vs','dribble_tackles_pct','dribbled_past','pressures','pressure_regain_pct','pressures_def_3rd','pressures_mid_3rd','pressures_att_3rd','blocks','blocked_shots','blocked_shots_saves','blocked_passes','interceptions','clearances','errors'],axis=1, errors='ignore')
   
    #CM stats
    if compareData == "CM":
        df_outfield = get_cm_data('https://fbref.com/en/comps/9/','/Premier-League-Stats')

        df_outfield = df_outfield[(df_outfield['player']==player1)  | (df_outfield['player']==player2)].reset_index()

        print(df_outfield['minutes_90s'])
        for x in range(len(df_outfield['player'])):
            if df_outfield['player'][x] == player1:
                squadPlayer1 = df_outfield['squad'].iloc[x]
                a_minutes90s = df_outfield['minutes_90s'][x]
                print("tjena tjena ")

            if df_outfield['player'][x] == player2:
                squadPlayer2 = df_outfield['squad'].iloc[x]
                b_minutes90s = df_outfield['minutes_90s'][x]

        df_outfield = df_outfield.drop(['index','nationality','position','squad','age','birth_year','minutes_90s','passes_completed','passes','passes_total_distance','passes_progressive_distance','passes_completed_short','passes_short','passes_pct_short','passes_completed_medium','passes_medium','passes_pct_medium','passes_completed_long','passes_long','passes_pct_long','assists','xa_per90','xa_net','_into_final_third','passes_into_penalty_area','crosses_into_penalty_area','progressive_passes','touches','touches_def_pen_area','touches_def_3rd','touches_mid_3rd','touches_att_3rd','touches_att_pen_area','touches_live_ball','dribbles_completed','dribbles','players_dribbled_past','nutmegs','carries','carry_distance','carry_progressive_distance','carries_into_penalty_area','pass_targets','passes_received','passes_received_pct','miscontrols','dispossessed','games','games_starts','minutes','goals','assists','pens_made','pens_att','cards_yellow','cards_red','goals_per90','assists_per90','goals_assists_per90','goals_pens_per90','goals_assists_pens_per90','xg','npxg','xa','xg_per90','xg_xa_per90','npxg_per90','npxg_xa_per90','nationality','position','squad','age','birth_year','cards_yellow','cards_red','cards_yellow_red','fouls','offsides','crosses','pens_won','pens_conceded','own_goals','ball_recoveries','aerials_won','aerials_lost','aerials_won_pct','tackles','tackles_won','tackles_def_3rd','tackles_mid_3rd','tackles_att_3rd','dribble_tackles','dribbles_vs','dribble_tackles_pct','dribbled_past','pressure_regain_pct','pressures_def_3rd','pressures_mid_3rd','pressures_att_3rd','blocks','blocked_shots','blocked_shots_saves','blocked_passes','interceptions','clearances','errors', 'passes_pct', 'dribbles_completed_pct'],axis=1, errors='ignore')

    #Fullback stats
    if compareData == "FB":
        df_outfield = get_fullback_data('https://fbref.com/en/comps/9/','/Premier-League-Stats')

        df_outfield = df_outfield[(df_outfield['player']==player1)  | (df_outfield['player']==player2)].reset_index()
        for x in range(len(df_outfield['player'])):
            if df_outfield['player'][x] == player1:
                squadPlayer1 = df_outfield['squad'].iloc[x]
                a_minutes90s = df_outfield['minutes_90s'][x]

            if df_outfield['player'][x] == player2:
                squadPlayer2 = df_outfield['squad'].iloc[x]
                b_minutes90s = df_outfield['minutes_90s'][x]

        df_outfield = df_outfield.drop(['index','nationality','position','squad','age','birth_year','games','games_starts','minutes','goals','assists','pens_made','pens_att','cards_yellow','cards_red','goals_per90','assists_per90','goals_assists_per90','goals_pens_per90','goals_assists_pens_per90','xg','npxg','xa','xg_per90','xa_per90','xg_xa_per90','npxg_per90','npxg_xa_per90', 'cards_yellow','cards_red','cards_yellow_red','fouled','offsides','crosses','tackles_won','pens_won','pens_conceded','own_goals','aerials_won','aerials_lost','tackles_won','tackles_def_3rd','tackles_mid_3rd','tackles_att_3rd','dribble_tackles','dribbles_vs','dribble_tackles_pct','dribbled_past','pressure_regains','pressure_regain_pct','pressures_def_3rd','pressures_mid_3rd','pressures_att_3rd','blocks','blocked_shots','blocked_shots_saves','blocked_passes','interceptions','clearances','errors', 'touches','touches_def_pen_area','touches_def_3rd','touches_mid_3rd','touches_att_3rd','touches_att_pen_area','touches_live_ball','dribbles','dribbles_completed_pct','players_dribbled_past','nutmegs','carries','carry_distance','carry_progressive_distance','carries_into_penalty_area','pass_targets','passes_received','passes_received_pct','miscontrols','dispossessed','passes_completed','passes','passes_total_distance','passes_progressive_distance','passes_completed_short','passes_short','passes_pct_short','passes_completed_medium','passes_medium','passes_pct_medium','passes_completed_long','passes_long','passes_pct_long','assists','xa','xa_net','passes_into_final_third','passes_into_penalty_area','progressive_passes', 'minutes_90s', 'passes_pct', 'aerials_won_pct'],axis=1, errors='ignore')




    #df_outfield = get_outfield_data('https://fbref.com/en/comps/9/','/Premier-League-Stats')


 

    
    



    df_outfield.to_csv('PL2021_Outfield.csv',index=False)

    #get parameters
    params = list(df_outfield.columns)
    params = params[1:]
    ranges = []
    a_values = []
    b_values = []

    for x in params:
       

        q = max(a_minutes90s,b_minutes90s)
        q2 = min(a_minutes90s,b_minutes90s)

        a = min(df_outfield[params][x])
        a = (a - (a*.25))/q2
        
        b = max(df_outfield[params][x])
        b = (b + (b*.25))/q
        
        ranges.append((a,b))
    quotients = []
    quotients2 = []


    for x in range(len(df_outfield['player'])):
        if df_outfield['player'][x] == player1:
            a_values = df_outfield.iloc[x].values.tolist()


        if df_outfield['player'][x] == player2:
            b_values = df_outfield.iloc[x].values.tolist()
            
    a_values = a_values[1:]
    for values in a_values:
        if a_minutes90s >= 1:
            quotients.append(values/a_minutes90s)
        else:
            quotients.append(values/1)

            print("cannot divide by 0")

    b_values = b_values[1:]
    for values in b_values:
        if b_minutes90s >= 1:
            quotients2.append(values/b_minutes90s)
        else:
            quotients2.append(values/1)

            print("cannot divide by zero")

    values = [quotients,quotients2]
    #title 

    title = dict(
        title_name=player1,
        title_color = 'red',
        subtitle_name = squadPlayer1,
        subtitle_color = 'red',
        title_name_2=player2,
        title_color_2 = 'blue',
        subtitle_name_2 = squadPlayer2,
        subtitle_color_2 = 'blue',
        title_fontsize = 18,
        subtitle_fontsize=15
    )
    # Setting the points for cropped image


    
    # Cropped image of above dimension
    # (It will not change original image)
    endnote = 'Jerome Planken'

    radar = Radar()

    fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,
                            radar_color=['red','blue'],
                            alphas=[.75,.6],title=title,endnote=endnote,
                            compare=True)
   

    fig.savefig('public/testing.png')
    im = Image.open('public/testing.png')

    def crop_center(pil_img, crop_width, crop_height):
        img_width, img_height = pil_img.size
     
        return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))
    im_new = crop_center(im, 800, 800)
    im_new.save('public/testing.png', quality=95)
   # img = Image.open('public/testing.png')

    #img.width

#    img = img.crop((4000, 2000, 5000, 5000))

 #   img.save('public/testing.png')




    return True

