#!/usr/bin/env python

import os
import sys

import pprint


def main():
    '''
    General axigen connection test
    '''
    from axigenapi import api as ax
    conn = ax.api('127.0.0.1')
    conn.connect()
    pprint.pprint(conn.get_version())
    del(conn)

    '''
    Axigen health check test
    '''
    from nimium import health
    hc = health.checks()
    if (hc.check_axigen('127.0.0.1') is True):
        print "Ok"
    else:
        print ("Failed: %s" % (hc.get_errors()))
    del(hc)

    '''
    Axigen succesful login test
    '''
    from nimium import axigenapi as ax
    conn = ax.axigenapi('127.0.0.1', timeout=3.0)
    username = sys.argv[1]
    password = sys.argv[2]
    if (conn.connect()):
        login = conn.login(username, password)
        if (login):
            print "OK"
        else:
            print conn.get_last_error()
            sys.exit(-1)
    help_content = conn.help()
    print "help content: %s" % (help_content)

    ## CONTEXT SWITCHING TESTCASE
    print "Post-prompt: %s" % (conn.get_prompt())
    print "Switch to server context: %s" % (conn.context_server())
    print "Switch to userdb context: %s" % (conn.context_server_userdb())
    print conn.back()
    print "Switch to AACL context: %s" % (conn.context_aacl())
    print conn.back()
    print "Switch to QUEUE context: %s" % (conn.context_queue())
    print conn.back()
    print "Switch to userdb context: %s" % (conn.context_server_userdb())
    print "List AllDomains: %s" % (conn.list_all_domains())
    print "Create Domain: %s" % (conn.create_domain(
        'domena\n\r\n1.hr', 'trl"""""ababalan'
    ))
    print "Set max accounts: %s" % (conn.set_max_accounts(
        "domena1.ba", 999999999999
    ))
    print "Returns: %s" % (conn.get_last_return())
    print "Error: %s" % (conn.get_last_error())

    ## DOMAIN MANAGEMENT TESTCASE
    print "Disable Domain: %s" % (conn.disable_domain('domena1.hr'))
    print "Disable N/A Domain: %s" % (conn.disable_domain('nepostoji.hr'))
    print "List AllDomains: %s" % (conn.list_all_domains())
    print "Delete Domain: %s" % (conn.delete_domain('domena1.hr'))
    print "Delete N/A Domain: %s" % (conn.delete_domain('nepostoji.hr'))
    print "List AllDomains: %s" % (conn.list_all_domains())

    ## DOMAIN E-MAILS TESTCASE
    print "List All accounts for nimiumdomain1.com: %s" % \
        (conn.list_all_accounts('nimiumdomain1.com'))
    print "Number of accounts for nimiumdomain1.com: %s" % \
        (conn.get_domain_utilization('nimiumdomain1.com'))
    print "Set limits: %s" % \
        (conn.set_max_accounts('nimiumdomain1.com', 15))
    print "Create accounts: %s" % \
       (conn.create_accounts('nimiumdomain1.com', [\
            {'user': 'ofac', 'password': 'blabla'},\
            {'user': 'mofac', 'password': 'blabla'},\
            {'user': 'pofac', 'password': 'pppp'},\
        ]))
    print "Number of accounts for nimiumdomain1.com: %s" % \
        (conn.get_domain_utilization('nimiumdomain1.com'))
    print "Change password: %s" % \
        (conn.change_account_password(
            'nimiumdomain2.com', 'postmaster', 'kvakvakva'
        )
    )

    ## DOMAIN ALIASES TESTCASE
    print "Domain aliases: %s" % \
        (conn.list_domain_aliases('nimiumdomain1.com'))
    print "Add domain alias: %s" % \
        (conn.add_domain_alias('nimiumdomain1.com', 'alaldomene.hr'))
    print "Domain aliases: %s" % \
        (conn.list_domain_aliases('nimiumdomain1.com'))
    print "Delete domain alias: %s" % \
        (conn.delete_domain_alias('nimiumdomain1.com', 'alaldomene.hr'))
    print "Domain aliases: %s" % \
        (conn.list_domain_aliases('nimiumdomain1.com'))
    print conn.back()

    ## AACL context testcase
    print "Domains of test user: %s" % \
        (conn.list_admin_domains('test-thorvat001'))

    del(conn)


def set_include_path():
    library_path = os.path.abspath("./")
    sys.path.append(library_path)


if __name__ == '__main__':
    set_include_path()
    main()
