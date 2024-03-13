import aiohttp
from typing import List, Dict
from dataclasses import dataclass, field
import json
import asyncio

@dataclass
class ChampionStats:
    hp: int
    hpperlevel: int
    mp: int
    mpperlevel: int
    movespeed: int
    armor: int
    armorperlevel: int
    spellblock: int
    spellblockperlevel: int
    attackrange: int
    hpregen: int
    hpregenperlevel: int
    mpregen: int
    mpregenperlevel: int
    crit: int
    critperlevel: int
    attackdamage: int
    attackdamageperlevel: int
    attackspeedperlevel: int
    attackspeed: int


@dataclass
class Champion:
    """По какой то непонятной мне причине id - это имя
    а key - это цифра - видимо то что я называю айди"""
    version: str
    id: str
    key: str
    name: str
    title: str
    blurb: str
    info: str
    image: str
    tags: str
    partype: str
    stats: ChampionStats

    @classmethod
    def load(cls, data: dict):
        data['stats'] = ChampionStats(**data['stats'])
        return cls(**data)


@dataclass
class Champions:
    by_name: Dict[str, Champion] = field(default_factory=dict)
    by_id: Dict[int, Champion] = field(default_factory=dict)

    @classmethod
    async def load_from_url(cls):
        url = 'https://ddragon.leagueoflegends.com/cdn/14.5.1/data/ru_RU/champion.json'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                result = await response.json()
        champs: Dict = result['data']
        by_name = {}
        by_id = {}
        for champ_name, champ_data in champs.items():
            obj = Champion.load(champ_data)
            by_name.update({obj.name: obj})
            by_id.update({int(obj.key): obj})
        return cls(by_name, by_id)


# champs_db = Champions.load_from_url()
# if __name__ == '__main__':
#     asyncio.run(Champions.load_from_url())
#
#
# @dataclass
# class ChampionMastery:
#     puuid: str
#     championPointsUntilNextLevel: int
#     chestGranted: bool
#     championId: int
#     lastPlayTime: int
#     championLevel: int
#     summonerId: str
#     championPoints: int
#     championPointsSinceLastLevel: int
#     tokensEarned: int
#
#
#
# user_puuid = 'j9eGWo7aDNcrCFSegcc1j0sPTCLiLLxU8z2JWRqoYcRA3Jr0nLXtmi08ySIttpTc1xJrVVdSXv4z7w'
# user_puuid = '9dUIxu1rGah-WAxCQ-LaDzWLb5lY_gjuI91r96HpLbuFlE06FANaIpeOJAKzt7RBuV4mklek3hlbNA'
# url = f'https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{user_puuid}?api_key=RGAPI-ca7ff195-03df-4712-b782-66158166f0f0'

# def main():
#     c
#
#
# if __name__ == '__main__':
#     main()