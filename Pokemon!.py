import random
from time import sleep

# import os
# import sys
# def restart():                     #这个是抄来的，重启程序，不过为什么没作用（但是好像用python本体打开有用？）
#     python=sys.executable             #本来想着有个重启程序的函数就不用用到fight这个大函数了，可以写到主程序里
#     os.execl(python, python, *sys.argv)

# 设置宝可梦属性值: HP生命值  ATK攻击力  DEF防御力  AVD闪避率  TYP属性  BUFF状态  LEFT大招剩余次数
# 属性：1:电  2：水  3：火  4：草   1>2>3>4>1
pokemon = ["皮卡丘", "杰尼龟", "小火龙", "妙蛙种子", "卡比兽"]
HP = {"皮卡丘": 80, "杰尼龟": 90, "小火龙": 80, "妙蛙种子": 100, "卡比兽": 110}
ATK = {"皮卡丘": 22, "杰尼龟": 20, "小火龙": 24, "妙蛙种子": 20, "卡比兽": 15}
DEF = {"皮卡丘": 7, "杰尼龟": 8, "小火龙": 7, "妙蛙种子": 9, "卡比兽": 9}
AVD = {"皮卡丘": 0.2, "杰尼龟": 0.1, "小火龙": 0.1, "妙蛙种子": 0.1, "卡比兽": 0.05}
TYP = {"皮卡丘": 1, "杰尼龟": 2, "小火龙": 3, "妙蛙种子": 4, "卡比兽": 3}
BUFF = {"皮卡丘": [], "杰尼龟": [], "小火龙": [], "妙蛙种子": [], "卡比兽": []}
LEFT={"皮卡丘":1,"杰尼龟":2,"小火龙":1,"妙蛙种子":1,"卡比兽":2}

def printer(strings):    # 逐字输出
    for char in strings:    #刚开始本来有用的，但后来发现太慢了，就没用了，但是蛮留着吧
        print(char, end='')
        sleep(0.1)

def intro_rule():
    print("----------规则介绍----------")
    sleep(1)
    print("每次战斗前，玩家可以选择三只宝可梦组成队伍，与电脑对战（电脑随机选择宝可梦），对战开始时选择一个宝可梦出战")
    sleep(1)
    print("由玩家先开始，玩家与电脑轮流行动，每回合可以从【攻击】、【净化】、【回复】、【替换】、【逃跑】中选择一项")
    sleep(1)
    print("每只宝可梦都有自己的属性、属性值以及技能，每个属性也有不同的特性")
    sleep(1)
    print("当宝可梦的生命值小于等于0时，将陷入[昏厥]，无法进行【攻击】、【净化】与【恢复】")
    sleep(1)
    print("当一方的所有宝可梦都陷入[昏厥]后，视为其战斗失败")
    sleep(1)
    print("最多进行20回合，20回合结束后，剩余宝可梦生命值总和最高的一方获胜")
    sleep(1)
    print(
        "【攻击】：从宝可梦技能中选择一项对目标进行攻击\n【回复】：（每场战斗（所有宝可梦）限1次），回复当前宝可梦30点生命值\n【净化】：（每场战斗限1次），清除当前宝可梦所有减益状态\n【替换】：从未[昏厥]的宝可梦中选择一只替换场上宝可梦，保留所有属性、状态\n【逃跑】：直接视为战斗失败")

def intro_type():
    print("共有电、水、火、草四个属性")
    sleep(1)
    print("其中：电 克制 水\t水 克制 火\t火 克制 草\t草 克制 电")
    sleep(1)
    print("目标属性被自身克制时，攻击额外造成30%伤害；目标属性克制自身时，攻击减少30%伤害\n")
    sleep(1.5)
    print("电属性特性：攻击命中后有30%概率永久赋予目标一层[感电]\n[感电]：受到伤害提升10%，最多叠加3层\n")
    sleep(1.5)
    print("水属性特性：受击后50%赋予自身一层[水形]\n[水形]：使自身闪避率提高10%，可无限叠加，成功闪避攻击后清空层数，并回复自身[水形]层数*5点生命值\n")
    sleep(1.5)
    print("火属性特性:攻击命中后有20%概率赋予目标[燃烧]2回合，火属性宝可梦对存在[燃烧]的目标造成的伤害额外提升15%\n[燃烧]：回合结束后受到5点伤害\n")
    sleep(1.5)
    print("草属性特性：回合结束后回复自身10%最大生命值,且有10%概率净化自身状态减益")

def intro_buff():
    print("----------状态减益----------")
    sleep(0.5)
    print("[昏厥]：无法进行【攻击】、【恢复】至本场战斗结束；若一名玩家所有宝可梦都陷入[昏厥]，则战斗失败\n[感电]：受到伤害提升10%，最多叠加3层\n[麻痹]:无法进行【攻击】\n[燃烧]：回合结束后受到3点伤害\n[中毒]：可无限叠加，回合结束受到[中毒]层数*5点伤害\n[眩晕]：无法行动")
    print()
    sleep(1)
    print("----------状态增益----------")
    sleep(0.5)
    print("[水形]：使自身闪避率提高10%，可无限叠加，成功闪避攻击后清空层数，并回复自身[水形]层数*5点生命值\n[引燃]：自身攻击命中后，赋予目标[燃烧]3回合；且自身对携带[燃烧]的目标造成的额外伤害提升至30%\n[百毒不侵]：受到拥有[中毒]的敌人的伤害减少20%")

def intro_pokemon(name):
    global HP, ATK, DEF, AVD, TYP
    if name == "皮卡丘":
        print("皮卡丘：电属性宝可梦\n")
        sleep(1)
        print(f"生命值：{HP["皮卡丘"]}  攻击力：{ATK["皮卡丘"]}  防御力：{DEF["皮卡丘"]}  闪避率：{AVD["皮卡丘"]}\n")
        sleep(1)
        print("技能一：电光一闪\n对目标造成100%攻击力电属性伤害，有20%概率连击一次，造成50%攻击力电属性伤害\n")
        sleep(1)
        print("技能二：十万伏特\n（每场战斗限1次）对目标造成160%攻击力电属性伤害；命中后有30%使目标[麻痹]一回合；目标每有一层[感电]，额外有20%概率使目标[麻痹]\n[麻痹]：无法进行【攻击】")
    elif name == "杰尼龟":
        print("杰尼龟：水属性宝可梦\n")
        sleep(1)
        print(f"生命值：{HP["杰尼龟"]}  攻击力：{ATK["杰尼龟"]}  防御力：{DEF["杰尼龟"]}  闪避率：{AVD["杰尼龟"]}\n")
        sleep(1)
        print("技能一：水枪\n对目标造成110%攻击力水属性伤害，攻击后有15%概率赋予自身一层[水形]\n")
        sleep(1)
        print("技能二：水之波动\n（每场战斗限2次）对目标造成160%攻击力水属性伤害，攻击后赋予自身一层[水形]")
    elif name == "小火龙":
        print("小火龙：火属性宝可梦\n")
        sleep(1)
        print(f"生命值：{HP["小火龙"]}  攻击力：{ATK["小火龙"]}  防御力：{DEF["小火龙"]}  闪避率：{AVD["小火龙"]}\n")
        sleep(1)
        print("技能一：火花\n对目标造成120%攻击力火属性伤害\n")
        sleep(1)
        print("技能二：龙之怒\n（每场战斗限一次）使自身获得[引燃]2回合，然后对目标造成160%攻击力伤害,命中后赋予目标[燃烧]2回合\n[引燃]：自身对携带[燃烧]的目标造成的额外伤害提升至30%")
    elif name == "妙蛙种子":
        print("妙蛙种子：草属性宝可梦\n")
        sleep(1)
        print(f"生命值：{HP["妙蛙种子"]}  攻击力：{ATK["妙蛙种子"]}  防御力：{DEF["妙蛙种子"]}  闪避率：{AVD["妙蛙种子"]}\n")
        sleep(1)
        print("技能一：毒粉\n对目标造成70%攻击力草属性伤害，命中后赋予目标一层[中毒]\n[中毒]：可无限叠加，回合结束受到[中毒]层数*3点伤害\n")
        sleep(1)
        print("技能二：寄生种子\n（每场战斗限1次）赋予目标2层[中毒]；赋予自身[百毒不侵]3回合\n[百毒不侵]：自身受到拥有[中毒]敌人的伤害降低20%")
    elif name == "卡比兽":
        print("卡比兽：火属性宝可梦\n")
        sleep(1)
        print(f"生命值：{HP["卡比兽"]}  攻击力：{ATK["卡比兽"]}  防御力：{DEF["卡比兽"]}  闪避率：{AVD["卡比兽"]}\n")
        sleep(1)
        print("技能一：撞击\n必中，对目标造成140%攻击力火属性伤害，有30%概率使目标[眩晕]一回合\n")
        sleep(1)
        print("技能二：百万吨重拳\n（每场战斗限两次）必中，对目标造成180%攻击力火属性伤害，有50%概率使目标[眩晕]一回合\n[眩晕]：无法行动")

def intro_game():
    print("-----------游戏介绍----------")
    print("规则介绍\t\t[输入1]\n属性介绍\t\t[输入2]\n状态介绍\t\t[输入3]\n宝可梦图鉴\t[输入4]\n其他任意键返回上一页")
    choice_intro = input("你的选择：")

    if choice_intro == "1":
        intro_rule()
        print()
        n = input("任意键返回上一页")
        intro_game()
    elif choice_intro == "2":
        intro_type()
        print()
        n = input("任意键返回上一页")
        intro_game()
    elif choice_intro == "3":
        intro_buff()
        print()
        n = input("任意键返回上一页")
        intro_game()
    elif choice_intro == "4":
        menu_pokemon()
        print()
        n = input("任意键返回上一页")
        menu_pokemon()
    else:
        menu()

def menu_pokemon():
    print("------宝可梦图鉴-----")
    print(
        "皮卡丘\t\t[输入1]\n杰尼龟\t\t[输入2]\n小火龙\t\t[输入3]\n妙蛙种子\t\t[输入4]\n卡比兽\t\t[输入5]\n其他任意键返回上一页")
    choice_pokemon = input("你的选择：")
    if choice_pokemon == "1":
        intro_pokemon("皮卡丘")
        print()
        n = input("任意键返回上一页")
        menu_pokemon()
    elif choice_pokemon == "2":
        intro_pokemon("杰尼龟")
        print()
        n = input("任意键返回上一页")
        menu_pokemon()
    elif choice_pokemon == "3":
        intro_pokemon("小火龙")
        print()
        n = input("任意键返回上一页")
        menu_pokemon()
    elif choice_pokemon == "4":
        intro_pokemon("妙蛙种子")
        print()
        n = input("任意键返回上一页")
        menu_pokemon()
    elif choice_pokemon == "5":
        intro_pokemon("卡比兽")
        print()
        n = input("任意键返回上一页")
        menu_pokemon()
    else:
        intro_game()

def atk(name_atk, name_def, atk_rate):
    global HP, ATK, DEF, AVD, TYP
    damage = (ATK[name_atk] - DEF[name_def]) * atk_rate
    if TYP[name_atk] == TYP[name_def] - 1 or (TYP[name_atk] == 4 and ATK[name_def] == 1):  # 克制/被克制：增伤/减伤30%
        damage *= 1.3
    elif TYP[name_def] == TYP[name_atk] - 1 or (TYP[name_def] == 4 and ATK[name_atk] == 1):
        damage *= 0.7
    damage=round(damage,2)
    return damage

def rate(r):            # 概率判断：在1~100内生成（r*100）个随机数，如果50在其中，则True
    n=r*100
    m=random.sample(range(1,100),int(n))
    if 50 in m:
        return True
    else:
        return False

def fight():
    global HP, ATK, DEF, AVD, TYP,BUFF,LEFT
    l_poke = ["", "皮卡丘", "杰尼龟", "小火龙", "妙蛙种子", "卡比兽"]
    def fight_exchange(re_player):
        print(f"请选择出战的宝可梦：")
        print(f"1.{player[0]}   2.{player[1]}   3.{player[2]}")
        f_p = f_player[int(input("你的选择："))]
        if f_p == re_player:
            print("这只宝可梦正在战斗！")
            skill(re_player)
        elif f_p != re_player:
            print(f"玩家用 {f_p} 替换了 {re_player} 出战！")
            return f_p

    def shui_get(victim, name):
        if name == "杰尼龟":
            get = rate(0.5)
            if get:
                if victim == "computer":
                    print(f"电脑的宝可梦 {now_computer} 获得一层[水形]！")
                    buff_computer.append("水形")
                elif victim == "player":
                    print(f"你的宝可梦 {now_player} 获得一层[水形]！")
                    now_player_buff.append("水形")

    def shui_clear(buff_list, name):
        print("攻击被闪避！")
        if name == "杰尼龟":
            if buff_list == buff_computer:
                restore = buff_computer.count("水形") * 5
                if hp_computer[now_computer] + restore <= HP[now_computer]:
                    hp_computer[now_computer] += restore
                else:
                    hp_computer[now_computer] = HP[now_computer]
            elif buff_list == now_player_buff:
                restore = now_player_buff.count("水形") * 5
                if hp_player[now_player] + restore <= HP[now_player]:
                    hp_player[now_player] += restore
                else:
                    hp_player[now_player] = HP[now_player]
            for i in range(1, 10):
                if buff_list == buff_computer:
                    if "水形" in buff_computer:
                        buff_computer.remove("水形")
                    else:
                        break
                elif buff_list == now_player_buff:
                    if "水形" in now_player_buff:
                        now_player_buff.remove("水形")
                    else:
                        break

    def pika(role):
        if role == "player":
            print(f"技能：    1.电光一闪      2.十万伏特（还剩{left_player["皮卡丘"]}次）")
            choice = int(input("你要使用："))

            if choice == 1:
                print("皮卡丘使用了 电光一闪！")
                combo = rate(0.2)
                miss = rate(avd_computer.get(now_computer))
                gandian = rate(0.3)
                sleep(0.5)
                if combo:
                    if miss:
                        shui_clear(buff_computer, now_computer)
                    else:
                        damage = atk("皮卡丘", now_computer, 1.0 + 0.1 * int(buff_computer.count("感电")))
                        print(f"攻击造成{damage}点伤害！")
                        hp_computer[now_computer] -= damage
                        if gandian:
                            print("目标获得一层[感电]！")
                            buff_computer.append("感电")
                            shui_get("computer", now_computer)
                    print("\n触发了连击！")
                    miss_combo = rate(avd_computer.get(now_computer))
                    sleep(0.5)
                    if miss_combo:
                        shui_clear(buff_computer, now_computer)
                    else:
                        damage_combo = atk("皮卡丘", now_computer, 0.5 + 0.1 * int(buff_computer.count("感电")))
                        print(f"连击造成{damage_combo}点伤害！")
                        gandian_combo = rate(0.3)
                        hp_computer[now_computer] -= damage_combo
                        if gandian_combo:
                            print("目标获得一层[感电]！")
                            buff_computer.append("感电")
                            shui_get("computer", now_computer)
                else:
                    if miss:
                        shui_clear(buff_computer, now_computer)
                    else:
                        damage = atk("皮卡丘", now_computer, 0.9 + 0.1 * int(buff_computer.count("感电")))
                        print(f"攻击造成{damage}点伤害！")
                        hp_computer[now_computer] -= damage
                        if gandian:
                            print("目标获得一层[感电]！")
                            buff_computer.append("感电")
                            shui_get("computer", now_computer)

            if choice == 2:
                if left_player.get("皮卡丘") == 1:
                    left_player["皮卡丘"] = 0
                    print("皮卡丘使用了 十万伏特！")
                    miss = rate(avd_computer.get(now_computer))
                    sleep(1)
                    if miss:
                        shui_clear(buff_computer, now_computer)
                    else:
                        damage = atk("皮卡丘", now_computer, 1.6 + 0.1 * int(buff_computer.count("感电")))
                        print(f"攻击造成{damage}点伤害！")
                        hp_computer[now_computer] -= damage
                        mabi = rate(0.3 + 0.2 * int(buff_computer.count("感电")))
                        if mabi:
                            print("目标陷入[麻痹]一回合！")
                            buff_computer.append("麻痹")
                        shui_get("computer", now_computer)
                else:
                    print("十万伏特 可用次数已耗尽！")
                    pika("player")
        if role == "computer":
            if now_player_buff.count("感电") <= 1:  # 如果目标感电层数小等于1，则用小技能
                print("皮卡丘使用了 电光一闪！")
                combo = rate(0.2)
                miss = rate(avd_player.get(now_player))
                gandian = rate(0.3)
                sleep(0.5)
                if combo:
                    if miss:
                        shui_clear(now_player_buff, now_player)
                    else:
                        damage = atk("皮卡丘", now_player, 1.0 + 0.1 * int(now_player_buff.count("感电")))
                        print(f"攻击造成{damage}点伤害！")
                        hp_player[now_player] -= damage
                        if gandian:
                            print("目标获得一层[感电]！")
                            now_player_buff.append("感电")
                            shui_get("player", now_player)
                    print("\n触发了连击！")
                    miss_combo = rate(avd_player.get(now_player))
                    sleep(0.5)
                    if miss_combo:
                        shui_clear(now_player_buff, now_player)
                    else:
                        damage_combo = atk("皮卡丘", now_player, 0.5 + 0.1 * int(now_player_buff.count("感电")))
                        print(f"连击造成{damage_combo}点伤害！")
                        gandian_combo = rate(0.3)
                        hp_player[now_player] -= damage_combo
                        if gandian_combo:
                            print("目标获得一层[感电]！")
                            now_player_buff.append("感电")
                        shui_get("player", now_player)
                else:
                    if miss:
                        shui_clear(now_player_buff, now_player)
                    else:
                        damage = atk("皮卡丘", now_player, 1.0 + 0.1 * int(now_player_buff.count("感电")))
                        print(f"攻击造成{damage}点伤害！")
                        hp_player[now_player] -= damage
                        if gandian:
                            print("目标获得一层[感电]！")
                            now_player_buff.append("感电")
                            shui_get("player", now_player)
            elif now_player_buff.count("感电") > 1:  # 如果目标感电层数大于1，则有80%概率开大
                sk2 = rate(0.8)
                if sk2 and left_computer["皮卡丘"] == 1:
                    left_computer["皮卡丘"] = 0
                    print("皮卡丘使用了 十万伏特！")
                    miss = rate(avd_player.get(now_player))
                    sleep(1)
                    if miss:
                        shui_clear(now_player_buff, now_player)
                    else:
                        damage = atk("皮卡丘", now_player, 1.6 + 0.1 * int(now_player_buff.count("感电")))
                        print(f"攻击造成{damage}点伤害！")
                        hp_player[now_player] -= damage
                        mabi = rate(0.3 + 0.2 * int(now_player_buff.count("感电")))
                        if mabi:
                            print("目标陷入[麻痹]一回合！")
                            now_player_buff.append("麻痹")
                        shui_get("player", now_player)
                else:
                    print("皮卡丘使用了 电光一闪！")
                    combo = rate(0.2)
                    miss = rate(avd_player.get(now_player))
                    gandian = rate(0.3)
                    sleep(0.5)
                    if combo:
                        if miss:
                            shui_clear(now_player_buff, now_player)
                        else:
                            damage = atk("皮卡丘", now_player, 1.0 + 0.1 * int(now_player_buff.count("感电")))
                            print(f"攻击造成{damage}点伤害！")
                            hp_player[now_player] -= damage
                            if gandian:
                                print("目标获得一层[感电]！")
                                now_player_buff.append("感电")
                                shui_get("player", now_player)
                        print("\n触发了连击！")
                        miss_combo = rate(avd_player.get(now_player))
                        sleep(0.5)
                        if miss_combo:

                            shui_clear(now_player_buff, now_player)
                        else:
                            damage_combo = atk("皮卡丘", now_player, 0.5 + 0.1 * int(now_player_buff.count("感电")))
                            print(f"连击造成{damage_combo}点伤害！")
                            gandian_combo = rate(0.3)
                            hp_player[now_player] -= damage_combo
                            if gandian_combo:
                                print("目标获得一层[感电]！")
                                now_player_buff.append("感电")
                            shui_get("player", now_player)

    def jieni(role):
        if role == "player":
            print(f"技能：     1.水枪    2.水之波动（剩余{left_player["杰尼龟"]}次）")
            choice = int(input("你要使用："))
            if choice == 1:
                print("杰尼龟使用了：  水枪！")
                shuixing = rate(0.15)
                miss = rate(avd_computer.get(now_computer))
                sleep(0.5)
                if miss:
                    shui_clear(buff_computer, now_computer)
                else:
                    damage = atk("杰尼龟", now_computer, 1.1)
                    print(f"攻击造成{damage}点伤害！")
                    hp_computer[now_computer] -= damage
                    shui_get("computer", now_computer)
                if shuixing:
                    now_player_buff.append("水形")
                    print("杰尼龟 [水形]层数+1")
                    avd_player["杰尼龟"] = avd_player["杰尼龟"] + 0.1

            elif choice == 2:
                if left_player["杰尼龟"] > 0:
                    left_player["杰尼龟"] -= 1
                    print("杰尼龟使用了：  水之波动！")
                    miss = rate(avd_computer.get(now_computer))
                    sleep(0.5)
                    if miss:
                        shui_clear(buff_computer, now_computer)
                    else:
                        damage = atk("杰尼龟", now_computer, 1.6)
                        print(f"攻击造成{damage}点伤害！")
                        hp_computer[now_computer] -= damage
                    now_player_buff.append("水形")
                    print("杰尼龟 [水形]层数+1")
                    avd_player["杰尼龟"] = avd_player["杰尼龟"] + 0.1
                    shui_get("computer", now_computer)
                else:
                    print("水之波动 可用次数已耗尽！")
                    jieni("player")
        elif role == "computer":
            if hp_computer.get(now_computer) >= 0.8 * HP.get(now_computer):  # 如果HP大于最大HP的80%，则用小技能
                print("杰尼龟使用了：  水枪！")
                shuixing = rate(0.15)
                miss = rate(avd_player.get(now_player))
                sleep(0.5)
                if miss:
                    shui_clear(now_player_buff, now_player)
                else:
                    damage = atk("杰尼龟", now_player, 1.1)
                    print(f"攻击造成{damage}点伤害！")
                    hp_player[now_player] -= damage
                    shui_get("player", now_player)
                if shuixing:
                    buff_computer.append("水形")
                    print("杰尼龟 [水形]层数+1")
                    avd_computer["杰尼龟"] = avd_computer["杰尼龟"] + 0.1
            else:
                sk2 = rate(0.6)  # 反之，有60%开大
                if sk2 and left_computer["杰尼龟"] > 0:
                    left_computer["杰尼龟"] -= 1
                    print("杰尼龟使用了：  水之波动！")
                    miss = rate(avd_player.get(now_player))
                    sleep(0.5)
                    if miss:
                        shui_clear(now_player_buff, now_player)
                    else:
                        damage = atk("杰尼龟", now_player, 1.6)
                        print(f"攻击造成{damage}点伤害！")
                        hp_player[now_player] -= damage
                    buff_computer.append("水形")
                    print("杰尼龟 [水形]层数+1")
                    avd_computer["杰尼龟"] = avd_computer["杰尼龟"] + 0.1
                    shui_get("player", now_player)
                else:
                    print("杰尼龟使用了：  水枪！")
                    shuixing = rate(0.15)
                    miss = rate(avd_player.get(now_player))
                    sleep(0.5)
                    if miss:
                        shui_clear(now_player_buff, now_player)
                    else:
                        damage = atk("杰尼龟", now_player, 1.1)
                        print(f"攻击造成{damage}点伤害！")
                        hp_player[now_player] -= damage
                        shui_get("player", now_player)
                    if shuixing:
                        buff_computer.append("水形")
                        print("杰尼龟 [水形]层数+1")
                        avd_computer["杰尼龟"] = avd_computer["杰尼龟"] + 0.1
                        shui_get("player", now_player)

    def huolong(role):
        if role == "player":
            print(f"技能:     1.火花        2.龙之怒（还剩{left_player["小火龙"]}次）")
            choice = int(input("你要使用："))
            if choice == 1:
                print("小火龙使用了 火花！")
                miss = rate(avd_computer.get(now_computer))
                fire = rate(0.2)
                sleep(0.5)
                if miss:
                    shui_clear(buff_computer, now_computer)
                else:
                    if "燃烧" in buff_computer:
                        a_rate = 1.2 + 0.15
                        if "引燃" in now_player_buff:
                            a_rate = 1.2 + 0.3
                    else:
                        a_rate = 1.2
                    damage = atk("小火龙", now_player, a_rate)
                    print(f"攻击造成{damage}点伤害！")
                    hp_computer[now_computer] -= damage
                    sleep(0.5)
                    if fire:
                        print("目标获得[燃烧]2回合！")
                        buff_computer.append("燃烧")
                        buff_computer.append("燃烧")
                    shui_get("computer", now_computer)

            elif choice == 2:
                if left_player.get("小火龙") == 1:
                    left_player["小火龙"] = 0
                    print("小火龙使用了 龙之怒！")
                    miss = rate(avd_computer.get(now_computer))
                    print("小火龙 获得[引燃]两回合！")
                    now_player_buff.append("引燃")
                    now_player_buff.append("引燃")
                    if miss:
                        shui_clear(buff_computer, now_computer)
                    else:
                        if "燃烧" in buff_computer:
                            b_rate = 1.6 + 0.3
                        else:
                            b_rate = 1.6
                        damage = atk("小火龙", now_computer, b_rate)
                        print(f"攻击造成{damage}点伤害！")
                        hp_computer[now_computer] -= damage
                        shui_get("computer", now_computer)
                else:
                    print("龙之怒 可用次数已耗尽！")
                    huolong("player")
        elif role == "computer":
            sk2 = rate(0.5)  # 50%概率开大
            if sk2 and left_computer["小火龙"] == 1:
                left_computer["小火龙"] = 0
                print("小火龙使用了 龙之怒！")
                miss = rate(avd_player.get(now_player))
                print("小火龙 获得[引燃]两回合！")
                buff_computer.append("引燃")
                buff_computer.append("引燃")
                if miss:
                    shui_clear(buff_computer, now_computer)
                else:
                    if "燃烧" in now_player_buff:
                        b_rate = 1.6 + 0.3
                    else:
                        b_rate = 1.6
                    damage = atk("小火龙", now_player, b_rate)
                    print(f"攻击造成{damage}点伤害！")
                    hp_player[now_player] -= damage
                    shui_get("player", now_player)
            else:
                print("小火龙使用了 火花！")
                miss = rate(avd_player.get(now_player))
                fire = rate(0.2)
                sleep(0.5)
                if miss:
                    shui_clear(now_player_buff, now_player)
                else:
                    if "燃烧" in now_player_buff:
                        a_rate = 1.2 + 0.15
                        if "引燃" in buff_computer:
                            a_rate = 1.2 + 0.3
                    else:
                        a_rate = 1.2
                    damage = atk("小火龙", now_player, a_rate)
                    print(f"攻击造成{damage}点伤害！")
                    hp_player[now_player] -= damage
                    sleep(0.5)
                    if "引燃" in buff_computer or fire:
                        print("目标获得[燃烧]2回合！")
                        now_player_buff.append("燃烧")
                        now_player_buff.append("燃烧")
                        shui_get("player", now_player)

    def miaowa(role):
        if role == "player":
            print(f"技能：     1.毒粉        2.寄生种子（还剩{left_player["妙蛙种子"]}次）")
            choice = int(input("你要使用："))
            if choice == 1:
                print("妙蛙种子使用了  毒粉！")
                miss = rate(avd_computer.get(now_computer))
                sleep(0.5)
                if miss:
                    shui_clear(buff_computer, now_computer)
                else:
                    damage = atk("妙蛙种子", now_computer, 0.7)
                    if "百毒不侵" in buff_computer and "中毒" in now_player_buff:
                        damage *= 0.8
                    print(f"攻击造成{damage}点伤害！")
                    print(f"电脑的宝可梦 {now_computer} 被赋予一层[中毒]！")
                    shui_get("computer", now_computer)
                    hp_computer[now_computer] -= damage
                    buff_computer.append("中毒")

            elif choice == 2:
                if left_player.get("妙蛙种子") == 1:
                    left_player["妙蛙种子"] = 0
                    print("妙蛙种子使用了  寄生种子！")
                    buff_computer.append("中毒")
                    buff_computer.append("中毒")
                    for i in range(4):
                        now_player_buff.append("百毒不侵")
                    print(
                        f"电脑的宝可梦 {now_computer} 被赋予2层[中毒]！    你的宝可梦 {now_player} 获得[百毒不侵]三回合！")
                else:
                    print("寄生种子 可用次数已耗尽！")
                    jieni("player")
        elif role == "computer":
            sk2 = rate(0.8)  # 80%概率开大
            if sk2 and left_computer["妙蛙种子"] == 1:
                left_computer["妙蛙种子"] = 0
                print("妙蛙种子使用了  寄生种子！")
                now_player_buff.append("中毒")
                now_player_buff.append("中毒")
                for i in range(4):
                    buff_computer.append("百毒不侵")
                print(
                    f"你的宝可梦 {now_player} 被赋予2层[中毒]！    电脑的宝可梦 {now_computer} 获得[百毒不侵]三回合！")
            else:
                print("妙蛙种子使用了  毒粉！")
                miss = rate(avd_player.get(now_player))
                sleep(0.5)
                if miss:
                    shui_clear(now_player_buff, now_player)
                else:
                    damage = atk("妙蛙种子", now_player, 0.7)
                    if "百毒不侵" in now_player_buff and "中毒" in buff_computer:
                        damage *= 0.8
                    print(f"攻击造成{damage}点伤害！")
                    print(f"你的宝可梦 {now_player} 被赋予一层[中毒]！")
                    hp_player[now_player] -= damage
                    now_player_buff.append("中毒")
                    shui_get("player", now_player)

    def kabi(role):
        if role == "player":
            print(f"技能：     1.撞击        2.百万吨重拳（还剩{left_player["卡比兽"]}次）")
            choice = int(input("你要使用："))
            fire = rate(0.2)
            if choice == 1:
                print("卡比兽使用了   撞击！")
                sleep(0.5)
                if "燃烧" in buff_computer:
                    damage = atk("卡比兽", now_computer, 1.4 + 0.15)
                else:
                    damage = atk("卡比兽", now_computer, 1.4)
                print(f"攻击造成{damage}点伤害！")
                hp_computer[now_computer] -= damage
                if fire:
                    sleep(0.5)
                    print("目标获得[燃烧]2回合！")
                    buff_computer.append("燃烧")
                    buff_computer.append("燃烧")
                dizzy = rate(0.3)
                if dizzy:
                    print("目标被[眩晕]！")
                    buff_computer.append("眩晕")
            elif choice == 2:
                if left_player["卡比兽"] == 0:
                    print("百万吨重拳 可用次数已耗尽！")
                    kabi("player")
                else:
                    left_player["卡比兽"] -= 1
                    print("卡比兽使用了   百万吨重拳！")
                    sleep(0.5)
                    dizzy = rate(0.5)
                    if "燃烧" in buff_computer:
                        damage = atk("卡比兽", now_computer, 1.8 + 0.15)
                    else:
                        damage = atk("卡比兽", now_computer, 1.8)
                    hp_computer[now_computer] -= damage
                    print(f"攻击造成{damage}点伤害！")
                    if fire:
                        sleep(0.5)
                        print("目标获得[燃烧]2回合！")
                        buff_computer.append("燃烧")
                        buff_computer.append("燃烧")
                    if dizzy:
                        print("目标被[眩晕]！")
                        buff_computer.append("眩晕")
            shui_get("computer", now_computer)
        elif role == "computer":
            fire = rate(0.2)
            if left_computer["卡比兽"] > 0:  # 直接大
                print("卡比兽使用了   百万吨重拳！")
                sleep(0.5)
                dizzy = rate(0.5)
                if "燃烧" in now_player_buff:
                    damage = atk("卡比兽", now_player, 1.8 + 0.15)
                else:
                    damage = atk("卡比兽", now_player, 1.8)
                hp_player[now_player] -= damage
                print(f"攻击造成{damage}点伤害！")
                if fire:
                    sleep(0.5)
                    print("目标获得[燃烧]2回合！")
                    now_player_buff.append("燃烧")
                    now_player_buff.append("燃烧")
                if dizzy:
                    print("目标被[眩晕]！")
                    now_player_buff.append("眩晕")
                shui_get("player", now_player)
            else:
                print("卡比兽使用了   撞击！")
                sleep(0.5)
                if "燃烧" in now_player_buff:
                    damage = atk("卡比兽", now_player, 1.4 + 0.15)
                else:
                    damage = atk("卡比兽", now_player, 1.4)
                print(f"攻击造成{damage}点伤害！")
                hp_player[now_player] -= damage
                if fire:
                    sleep(0.5)
                    print("目标获得[燃烧]2回合！")
                    now_player_buff.append("燃烧")
                    now_player_buff.append("燃烧")
                dizzy = rate(0.3)
                if dizzy:
                    print("目标被[眩晕]！")
                    now_player_buff.append("眩晕")
                shui_get("player", now_player)

    def skill(name):
        if name == "皮卡丘":
            pika("player")
        elif name == "杰尼龟":
            jieni("player")
        elif name == "小火龙":
            huolong("player")
        elif name == "妙蛙种子":
            miaowa("player")
        elif name == "卡比兽":
            kabi("player")

    c = random.sample(range(1, 6), 3)  # 电脑随机选择3只
    computer = [l_poke[c[0]], l_poke[c[1]], l_poke[c[2]]]
    print("请选择三只宝可梦组成队伍（空格分开）：")
    print("1.皮卡丘    2.杰尼龟    3.小火龙    4.妙蛙种子    5.卡比兽")
    try:
        ch_p1, ch_p2, ch_p3 = map(int, input("你的选择：").split())  # 玩家选择3只
        if ch_p1 == ch_p2 or ch_p2 == ch_p3 or ch_p3 == ch_p1:  # 用户总是会做出一些意想不到的输入：有人选了三只皮卡丘
            print("选择的宝可梦重复了！请重新选择!\n")
            fight()
        player = [l_poke[ch_p1], l_poke[ch_p2], l_poke[ch_p3]]
    except Exception as e:
        print("干啥呢？\n")
        menu()

    # 初始化属性值    名字：属性值
    hp_player = {f"{l_poke[ch_p1]}": HP.get(l_poke[ch_p1]), f"{l_poke[ch_p2]}": HP.get(l_poke[ch_p2]),f"{l_poke[ch_p3]}": HP.get(l_poke[ch_p3])}  # 用f"{}"的形式：让我知道这玩意是个字符串
    atk_player = {f"{l_poke[ch_p1]}": ATK.get(l_poke[ch_p1]), f"{l_poke[ch_p2]}": ATK.get(l_poke[ch_p2]),f"{l_poke[ch_p3]}": ATK.get(l_poke[ch_p3])}  # 不太确定这些后面会不会用到，但是蛮蛮写了吧 反正都是ctrl c+v
    def_player = {f"{l_poke[ch_p1]}": DEF.get(l_poke[ch_p1]), f"{l_poke[ch_p2]}": DEF.get(l_poke[ch_p2]),f"{l_poke[ch_p3]}": DEF.get(l_poke[ch_p3])}  # 时间或许是初学者最没用的东西
    avd_player = {f"{l_poke[ch_p1]}": AVD.get(l_poke[ch_p1]), f"{l_poke[ch_p2]}": AVD.get(l_poke[ch_p2]),f"{l_poke[ch_p3]}": AVD.get(l_poke[ch_p3])}  # 我为什么要在注释里写这些。。？
    typ_player = {f"{l_poke[ch_p1]}": TYP.get(l_poke[ch_p1]), f"{l_poke[ch_p2]}": TYP.get(l_poke[ch_p2]),f"{l_poke[ch_p3]}": TYP.get(l_poke[ch_p3])}
    buff_player = {f"{l_poke[ch_p1]}": [], f"{l_poke[ch_p2]}": [], f"{l_poke[ch_p3]}": []}
    left_player = {f"{l_poke[ch_p1]}": LEFT.get(l_poke[ch_p1]), f"{l_poke[ch_p2]}": LEFT.get(l_poke[ch_p2]),f"{l_poke[ch_p3]}": LEFT.get(l_poke[ch_p3])}
    hp_computer = {f"{l_poke[c[0]]}": HP.get(l_poke[c[0]]), f"{l_poke[c[1]]}": HP.get(l_poke[c[1]]),f"{l_poke[c[2]]}": HP.get(l_poke[c[2]])}
    atk_computer = {f"{l_poke[c[0]]}": ATK.get(l_poke[c[0]]), f"{l_poke[c[1]]}": ATK.get(l_poke[c[1]]),f"{l_poke[c[2]]}": ATK.get(l_poke[c[2]])}
    def_computer = {f"{l_poke[c[0]]}": DEF.get(l_poke[c[0]]), f"{l_poke[c[1]]}": DEF.get(l_poke[c[1]]),f"{l_poke[c[2]]}": DEF.get(l_poke[c[2]])}
    avd_computer = {f"{l_poke[c[0]]}": AVD.get(l_poke[c[0]]), f"{l_poke[c[1]]}": AVD.get(l_poke[c[1]]),f"{l_poke[c[2]]}": AVD.get(l_poke[c[2]])}
    type_computer = {f"{l_poke[c[0]]}": TYP.get(l_poke[c[0]]), f"{l_poke[c[1]]}": TYP.get(l_poke[c[1]]),f"{l_poke[c[2]]}": TYP.get(l_poke[c[2]])}
    left_computer = {f"{l_poke[c[0]]}": LEFT.get(l_poke[c[0]]), f"{l_poke[c[1]]}": LEFT.get(l_poke[c[1]]),f"{l_poke[c[2]]}": LEFT.get(l_poke[c[2]])}
    buff_computer = []  # 本来还是用字典的，方便电脑换人；但是后面感觉让电脑换人太麻烦了，就没让它换（或者我菜），但是上面那些电脑的字典已经被调用过了，就没改（懒）
    clean_player = 1
    clean_computer = 1
    cure_player = 1
    cure_computer = 1

    print("请选择出战的宝可梦：")
    print(f"1.{player[0]}   2.{player[1]}   3.{player[2]}")
    f_player = ["", f"{player[0]}", f"{player[1]}", f"{player[2]}"]
    try:
        f_p1 = int(input("你的选择："))
        print()
        print(f"你选择了 {f_player[f_p1]}!")
    except Exception as e:
        print("干啥呢\n")
        menu()
    print(f"电脑选择了 {computer[0]}!")
    now_player = f_player[f_p1]
    now_computer = computer[0]
    now_player_buff = buff_player.get(now_player)  # 将出战宝可梦的buff搞到一个列表里，有几层buff列表中就有几个同名元素，到时候需要的时候删一个即可;新搞一个列表是为了方便换人的时候同时把状态也换掉
    for i in range(1, 21):
        print()
        s_hp_player = {i for i in hp_player.values()}  # 用字典.values函数得到的竟然是个没见过的数据类型dict_values(),这样的话还得把这里面的元素遍历到一个其他数据容器里，好奇怪
        s_hp_computer = {i for i in hp_computer.values()}
        if (len(s_hp_computer) == 1 and s_hp_computer.pop() == 0) or (len(s_hp_player) == 1 and s_hp_player.pop() == 0):  # 如果任意一方生命值集合中唯一元素为0，则游戏结束
            print("战斗结束")
            if len(s_hp_computer) == 1 and s_hp_computer.pop() == 0:
                print("玩家获胜！")
            elif len(s_hp_player) == 1 and s_hp_player.pop() == 0:
                print("电脑获胜！")
            break
        sleep(1)
        print("-----你的回合-----")
        def your_turn(buff):
            if buff in now_player_buff:
                return True
            else:
                return False
        if your_turn("昏厥"):
            print("当前宝可梦已昏厥！")
            print("你想要进行：\n4.替换     6.逃跑")
            now_player_buff.remove("昏厥")
        elif your_turn("眩晕"):
            print("当前宝可梦陷入眩晕！无法行动！！")
            print("你想要进行：\n5.空过    6.逃跑")
            now_player_buff.remove("眩晕")
        elif your_turn("麻痹"):
            print("当前宝可梦被麻痹！无法攻击！")
            print(f"你想要进行：\n2.净化（还剩{clean_player}次）    3.回复（还剩{cure_player}次）     4.替换    5.空过     6.逃跑")
            now_player_buff.remove("麻痹")
        else:
            print(f"你想要进行：\n1.攻击    2.净化（还剩{clean_player}次）   3.回复（还剩{cure_player}次）     4.替换    5.空过     6.逃跑")
        choice_move = input("你的选择：")
        choice_correct=False
        if (your_turn("昏厥")) and (choice_move=="4" or "6"):
            choice_correct=True
        elif (your_turn("眩晕")) and (choice_move=="5" or "6"):
            choice_correct=True
        elif (your_turn("麻痹")) and (choice_move=="2" or "3" or "4" or "5" or "6"):
            choice_correct=True
        elif choice_move=="1" or "2" or "3" or "4" or "5" or "6":
            choice_correct=True

        if choice_correct:
            if choice_move == "1":
                skill(now_player)
                if hp_computer.get(now_computer) <= 0:
                    print(f"电脑的宝可梦 {now_computer} 陷入昏厥！")
            elif choice_move == "2":
                if clean_player == 1:
                    for i in range(51):  # 最多净化50个 应该够吧。。
                        if "感电" in now_player_buff:
                            now_player_buff.remove("感电")
                        elif "麻痹" in now_player_buff:
                            now_player_buff.remove("麻痹")
                        elif "燃烧" in now_player_buff:
                            now_player_buff.remove("燃烧")
                        elif "中毒" in now_player_buff:
                            now_player_buff.remove("中毒")
                        else:
                            break
                    print("已清空状态减益！")
                    clean_player = 0
                else:
                    print("次数都没了还选，罚你空过")
            elif choice_move == "3":
                if cure_player == 1:
                    if hp_player[now_player] + 30 <= HP[now_player]:
                        hp_player[now_player] += 30
                    else:
                        hp_player[now_player] = HP[now_player]
                    print(f"你的宝可梦 {now_player} 已回复30点HP,当前HP：{hp_player[now_player]}")
                    cure_player = 0
                else:
                    print("次数都没了了还选，罚你空过")
            elif choice_move == "4":
                buff_player[now_player] = now_player_buff  # 先将当前宝可梦的状态储存到字典里
                now_player = fight_exchange(now_player)  # 再换人
                now_player_buff = buff_player.get(now_player)  # 再将换后宝可梦的状态取出
            elif choice_move == "5":
                print()
            elif choice_move == "6":
                print("玩家逃跑！战斗失败！")
                break
        else:
            print("选啥呢，罚你空过")
        if "燃烧" in now_player_buff:  # 玩家的计回合的buff在回合结束后-1
            hp_player[now_player] = hp_player.get(now_player) - 5
            now_player_buff.remove("燃烧")
            print(f"{now_player} 由于[燃烧]失去5点HP！")
        if "引燃" in now_player_buff:
            now_player_buff.remove("引燃")
        if "中毒" in now_player_buff:
            hp_player[now_player] = hp_player.get(now_player) - 3 * now_player_buff.count("中毒")
            print(f"    {now_player} 由于[中毒]失去{5 * now_player_buff.count("中毒")}点HP！")
        if "百毒不侵" in now_player_buff:
            now_player_buff.remove("百毒不侵")
        print(
            f"电脑的宝可梦 {now_computer} 剩余HP：{hp_computer.get(now_computer)}")  # 本来还想print状态集合的，但是可能这样就print得太长了，所以就没搞（反正也没几个，应该能记得差不多）
        if typ_player.get(now_player) == 4:  # 考虑用户体验真的麻烦，所以我准备少考虑一点（）
            if hp_player.get(now_player) * 1.1 <= HP.get(now_player):
                hp_player[now_player] *= 1.1
            else:
                hp_player[now_player] = HP.get(now_player)
            clean = rate(0.1)
            if clean:
                for i in range(101):
                    if "感电" in now_player_buff:
                        now_player_buff.remove("感电")
                    elif "麻痹" in now_player_buff:
                        now_player_buff.remove("麻痹")
                    elif "燃烧" in now_player_buff:
                        now_player_buff.remove("燃烧")
                    elif "中毒" in now_player_buff:
                        now_player_buff.remove("中毒")
                    else:
                        break
        sleep(1)

        print()
        print("-----电脑的回合-----")
        if hp_computer[now_computer] <= 0:
            print(f"电脑的宝可梦 {now_computer} 已陷入昏厥！")
            print(f"电脑用 {computer[computer.index(now_computer) + 1]} 替换了 {now_computer}!")
            now_computer = computer[computer.index(now_computer) + 1]
            buff_computer.clear()
        if "昏厥" in buff_computer:
            print(f"电脑的宝可梦 {now_computer} 已昏厥！")
            print(f"电脑用 {computer[computer.index(now_computer) + 1]} 替换了 {now_computer} 出战！")
            now_computer = computer[computer.index(now_computer) + 1]  # 电脑的宝可梦要是昏了就换下一个
        if "眩晕" in buff_computer:
            print(f"电脑的宝可梦 {now_computer} 被眩晕，无法行动！")
            buff_computer.remove("眩晕")
            continue
        if len(buff_computer) >= 6 and clean_computer == 1:  # 状态太多（>=6）则净化
            for i in range(51):
                if "感电" in buff_computer:
                    buff_computer.remove("感电")
                elif "麻痹" in buff_computer:
                    buff_computer.remove("麻痹")
                elif "燃烧" in buff_computer:
                    buff_computer.remove("燃烧")
                elif "中毒" in buff_computer:
                    buff_computer.remove("中毒")
                else:
                    break
            print(f"电脑的宝可梦 {now_computer} 已清空状态减益！")
            clean_computer = 0
        if "麻痹" in buff_computer:
            print(f"电脑的宝可梦 {now_computer} 被麻痹了！ ")
            if hp_computer[now_computer] <= 50 and cure_computer == 1:  # 被麻痹且血少于50，回血
                hp_computer[now_computer] += 30
                cure_computer = 0
                print(f"电脑的宝可梦 {now_computer} 陷入麻痹，但选择回复30点HP\n当前HP：{hp_computer[now_computer]}")
            else:
                print(f"电脑的宝可梦 {now_computer} 陷入麻痹,并选择空过")
        if hp_computer[now_computer] <= 30 and cure_computer == 1 and now_computer == computer[
            1]:  # 是电脑的第二只，且能行动但血少于30，回血
            hp_computer[now_computer] += 30
            cure_computer = 0
        else:
            if now_computer == "皮卡丘":
                pika("computer")
            elif now_computer == "杰尼龟":
                jieni("computer")
            elif now_computer == "小火龙":
                huolong("computer")
            elif now_computer == "妙蛙种子":
                miaowa("computer")
            elif now_computer == "卡比兽":
                kabi("computer")

            if "燃烧" in buff_computer:
                hp_computer[now_computer] = hp_computer.get(now_computer) - 5
                buff_computer.remove("燃烧")
                print(f"{now_computer} 由于[燃烧]失去5点HP！")
            if "引燃" in buff_computer:
                buff_computer.remove("引燃")
            if "中毒" in buff_computer:
                hp_computer[now_computer] = hp_computer.get(now_computer) - 5 * buff_computer.count("中毒")
                print(f"{now_computer} 由于[中毒]失去{3 * buff_computer.count("中毒")}点HP！")
            if "百毒不侵" in buff_computer:
                buff_computer.remove("百毒不侵")

            if hp_player[now_player] > 0:
                print(f"你的宝可梦 {now_player} 剩余HP：{hp_player[now_player]}")
            else:
                now_player_buff.append("昏厥")
            if type_computer.get(now_computer) == 4:  # 考虑用户体验真的麻烦，所以我准备少考虑一点（）
                if hp_computer.get(now_computer) * 1.1 <= HP.get(now_computer):
                    hp_computer[now_computer] *= 1.1
                else:
                    hp_computer[now_computer] = HP.get(now_computer)
                clean = rate(0.1)
                if clean:
                    for i in range(101):
                        if "感电" in buff_computer:
                            buff_computer.remove("感电")
                        elif "麻痹" in buff_computer:
                            buff_computer.remove("麻痹")
                        elif "燃烧" in buff_computer:
                            buff_computer.remove("燃烧")
                        elif "中毒" in buff_computer:
                            buff_computer.remove("中毒")
                        else:
                            break
            sleep(1)
            print()
            s_buff_p = set()
            s_buff_c = set()  # 想了想 还是print状态吧，但是就不显示层数（回合数）了，因为我的层数（回合数）是通过状态名在列表中的数量体现的，所以显示层数（回合数）的话就会很长
            s_buff_p.clear()  # 将状态列表中的状态取出，加入状态集合中，以去重，并且在每次操作前清空集合，防止上一回合的状态污染这一回合的状态集合
            s_buff_c.clear()
            for i in now_player_buff:
                s_buff_p.add(i)
            for i in buff_computer:
                s_buff_c.add(i)
            print(f"你的宝可梦现在的状态集合：{s_buff_p}")
            print(f"电脑的宝可梦现在的状态集合：{s_buff_c}")

def menu():
    print("----------宝可梦对战----------")
    print("开始游戏\t\t[输入1]\n游戏介绍\t\t[输入2]\n退出游戏\t\t[输入3]")
    choice_menu =input("你的选择：")
    if choice_menu == "1":
        fight()
    elif choice_menu == "2":
        intro_game()
    elif choice_menu == "3":
        print("已退出！")
    else:
        print("干啥呢\n")
        menu()

menu()