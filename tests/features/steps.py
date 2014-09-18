# -*- coding: utf-8 -*-
from lettuce import *
import app.match as m


@step('Given: "([^"]*)" and "([^"]*)" start a match to "([^"]*)" sets')
def given_group1_and_group2_start_a_match_to_group3_sets(step, p1, p2, s):
    world.match = m.Match(p1, p2, s)


@step('Then: I see score: "([^"]*)"')
def then_i_see_score_group1(step, set):
    assert world.match.score() == set, \
        "Got %s" % world.match.score()


@step('When: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def when_group1_won_the_group2_set_group3_group4(step, w, s, s1, s2):
    world.match.won_set(w, s, s1, s2)


@step('And: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def and_group1_won_the_group2_set_group3_group4(step, w, s, s1, s2):
    world.match.won_set(w, s, s1, s2)


@step('Then: The match score is: "([^"]*)"')
def then_the_match_score_is_group1(step, res):
    assert world.match.resultados() == res, \
        "Got %s" % world.match.resultados()
