const countries = [{ 'Name': 'Afghanistan', 'Code': 'AFG', 'Flag': 'af.png' },
{ 'Name': 'Albania', 'Code': 'ALB', 'Flag': 'al.png' },
{ 'Name': 'Algeria', 'Code': 'DZA', 'Flag': 'dz.png' },
{ 'Name': 'American Samoa', 'Code': 'ASM', 'Flag': 'as.png' },
{ 'Name': 'Andorra', 'Code': 'AND', 'Flag': 'ad.png' },
{ 'Name': 'Angola', 'Code': 'AGO', 'Flag': 'ao.png' },
{ 'Name': 'Anguilla', 'Code': 'AIA', 'Flag': 'ai.png' },
{ 'Name': 'Antarctica', 'Code': 'ATA', 'Flag': 'aq.png' },
{ 'Name': 'Antigua and Barbuda', 'Code': 'ATG', 'Flag': 'ag.png' },
{ 'Name': 'Argentina', 'Code': 'ARG', 'Flag': 'ar.png' },
{ 'Name': 'Armenia', 'Code': 'ARM', 'Flag': 'am.png' },
{ 'Name': 'Aruba', 'Code': 'ABW', 'Flag': 'aw.png' },
{ 'Name': 'Australia', 'Code': 'AUS', 'Flag': 'au.png' },
{ 'Name': 'Austria', 'Code': 'AUT', 'Flag': 'at.png' },
{ 'Name': 'Azerbaijan', 'Code': 'AZE', 'Flag': 'az.png' },
{ 'Name': 'Bahamas', 'Code': 'BHS', 'Flag': 'bs.png' },
{ 'Name': 'Bahrain', 'Code': 'BHR', 'Flag': 'bh.png' },
{ 'Name': 'Bangladesh', 'Code': 'BGD', 'Flag': 'bd.png' },
{ 'Name': 'Barbados', 'Code': 'BRB', 'Flag': 'bb.png' },
{ 'Name': 'Belarus', 'Code': 'BLR', 'Flag': 'by.png' },
{ 'Name': 'Belgium', 'Code': 'BEL', 'Flag': 'be.png' },
{ 'Name': 'Belize', 'Code': 'BLZ', 'Flag': 'bz.png' },
{ 'Name': 'Benin', 'Code': 'BEN', 'Flag': 'bj.png' },
{ 'Name': 'Bermuda', 'Code': 'BMU', 'Flag': 'bm.png' },
{ 'Name': 'Bhutan', 'Code': 'BTN', 'Flag': 'bt.png' },
{ 'Name': 'Bolivia', 'Code': 'BOL', 'Flag': 'bo.png' },
{ 'Name': 'Bosnia and Herzegovina', 'Code': 'BIH', 'Flag': 'ba.png' },
{ 'Name': 'Botswana', 'Code': 'BWA', 'Flag': 'bw.png' },
{ 'Name': 'Brazil', 'Code': 'BRA', 'Flag': 'br.png' },
{ 'Name': 'British Indian Ocean Territory', 'Code': 'IOT', 'Flag': 'io.png' },
{ 'Name': 'British Virgin Islands', 'Code': 'VGB', 'Flag': 'vg.png' },
{ 'Name': 'Brunei', 'Code': 'BRN', 'Flag': 'bn.png' },
{ 'Name': 'Bulgaria', 'Code': 'BGR', 'Flag': 'bg.png' },
{ 'Name': 'Burkina Faso', 'Code': 'BFA', 'Flag': 'bf.png' },
{ 'Name': 'Burundi', 'Code': 'BDI', 'Flag': 'bi.png' },
{ 'Name': 'Cambodia', 'Code': 'KHM', 'Flag': 'kh.png' },
{ 'Name': 'Cameroon', 'Code': 'CMR', 'Flag': 'cm.png' },
{ 'Name': 'Canada', 'Code': 'CAN', 'Flag': 'ca.png' },
{ 'Name': 'Cape Verde', 'Code': 'CPV', 'Flag': 'cv.png' },
{ 'Name': 'Cayman Islands', 'Code': 'CYM', 'Flag': 'ky.png' },
{ 'Name': 'Central African Republic', 'Code': 'CAF', 'Flag': 'cf.png' },
{ 'Name': 'Chad', 'Code': 'TCD', 'Flag': 'td.png' },
{ 'Name': 'Chile', 'Code': 'CHL', 'Flag': 'cl.png' },
{ 'Name': 'China', 'Code': 'CHN', 'Flag': 'cn.png' },
{ 'Name': 'Christmas Island', 'Code': 'CXR', 'Flag': 'cx.png' },
{ 'Name': 'Cocos Islands', 'Code': 'CCK', 'Flag': 'cc.png' },
{ 'Name': 'Colombia', 'Code': 'COL', 'Flag': 'co.png' },
{ 'Name': 'Comoros', 'Code': 'COM', 'Flag': 'km.png' },
{ 'Name': 'Cook Islands', 'Code': 'COK', 'Flag': 'ck.png' },
{ 'Name': 'Costa Rica', 'Code': 'CRI', 'Flag': 'cr.png' },
{ 'Name': 'Croatia', 'Code': 'HRV', 'Flag': 'hr.png' },
{ 'Name': 'Cuba', 'Code': 'CUB', 'Flag': 'cu.png' },
{ 'Name': 'Curacao', 'Code': 'CUW', 'Flag': 'cw.png' },
{ 'Name': 'Cyprus', 'Code': 'CYP', 'Flag': 'cy.png' },
{ 'Name': 'Czech Republic', 'Code': 'CZE', 'Flag': 'cz.png' },
{ 'Name': 'Democratic Republic of the Congo', 'Code': 'COD', 'Flag': 'cd.png' },
{ 'Name': 'Denmark', 'Code': 'DNK', 'Flag': 'dk.png' },
{ 'Name': 'Djibouti', 'Code': 'DJI', 'Flag': 'dj.png' },
{ 'Name': 'Dominica', 'Code': 'DMA', 'Flag': 'dm.png' },
{ 'Name': 'Dominican Republic', 'Code': 'DOM', 'Flag': 'do.png' },
{ 'Name': 'East Timor', 'Code': 'TLS', 'Flag': 'tl.png' },
{ 'Name': 'Ecuador', 'Code': 'ECU', 'Flag': 'ec.png' },
{ 'Name': 'Egypt', 'Code': 'EGY', 'Flag': 'eg.png' },
{ 'Name': 'El Salvador', 'Code': 'SLV', 'Flag': 'sv.png' },
{ 'Name': 'Equatorial Guinea', 'Code': 'GNQ', 'Flag': 'gq.png' },
{ 'Name': 'Eritrea', 'Code': 'ERI', 'Flag': 'er.png' },
{ 'Name': 'Estonia', 'Code': 'EST', 'Flag': 'ee.png' },
{ 'Name': 'Ethiopia', 'Code': 'ETH', 'Flag': 'et.png' },
{ 'Name': 'Falkland Islands', 'Code': 'FLK', 'Flag': 'fk.png' },
{ 'Name': 'Faroe Islands', 'Code': 'FRO', 'Flag': 'fo.png' },
{ 'Name': 'Fiji', 'Code': 'FJI', 'Flag': 'fj.png' },
{ 'Name': 'Finland', 'Code': 'FIN', 'Flag': 'fi.png' },
{ 'Name': 'France', 'Code': 'FRA', 'Flag': 'fr.png' },
{ 'Name': 'French Polynesia', 'Code': 'PYF', 'Flag': 'pf.png' },
{ 'Name': 'Gabon', 'Code': 'GAB', 'Flag': 'ga.png' },
{ 'Name': 'Gambia', 'Code': 'GMB', 'Flag': 'gm.png' },
{ 'Name': 'Georgia', 'Code': 'GEO', 'Flag': 'ge.png' },
{ 'Name': 'Germany', 'Code': 'DEU', 'Flag': 'de.png' },
{ 'Name': 'Ghana', 'Code': 'GHA', 'Flag': 'gh.png' },
{ 'Name': 'Gibraltar', 'Code': 'GIB', 'Flag': 'gi.png' },
{ 'Name': 'Greece', 'Code': 'GRC', 'Flag': 'gr.png' },
{ 'Name': 'Greenland', 'Code': 'GRL', 'Flag': 'gl.png' },
{ 'Name': 'Grenada', 'Code': 'GRD', 'Flag': 'gd.png' },
{ 'Name': 'Guam', 'Code': 'GUM', 'Flag': 'gu.png' },
{ 'Name': 'Guatemala', 'Code': 'GTM', 'Flag': 'gt.png' },
{ 'Name': 'Guernsey', 'Code': 'GGY', 'Flag': 'gg.png' },
{ 'Name': 'Guinea', 'Code': 'GIN', 'Flag': 'gn.png' },
{ 'Name': 'Guinea-Bissau', 'Code': 'GNB', 'Flag': 'gw.png' },
{ 'Name': 'Guyana', 'Code': 'GUY', 'Flag': 'gy.png' },
{ 'Name': 'Haiti', 'Code': 'HTI', 'Flag': 'ht.png' },
{ 'Name': 'Honduras', 'Code': 'HND', 'Flag': 'hn.png' },
{ 'Name': 'Hong Kong', 'Code': 'HKG', 'Flag': 'hk.png' },
{ 'Name': 'Hungary', 'Code': 'HUN', 'Flag': 'hu.png' },
{ 'Name': 'Iceland', 'Code': 'ISL', 'Flag': 'is.png' },
{ 'Name': 'India', 'Code': 'IND', 'Flag': 'in.png' },
{ 'Name': 'Indonesia', 'Code': 'IDN', 'Flag': 'id.png' },
{ 'Name': 'Iran', 'Code': 'IRN', 'Flag': 'ir.png' },
{ 'Name': 'Iraq', 'Code': 'IRQ', 'Flag': 'iq.png' },
{ 'Name': 'Ireland', 'Code': 'IRL', 'Flag': 'ie.png' },
{ 'Name': 'Isle of Man', 'Code': 'IMN', 'Flag': 'im.png' },
{ 'Name': 'Israel', 'Code': 'ISR', 'Flag': 'il.png' },
{ 'Name': 'Italy', 'Code': 'ITA', 'Flag': 'it.png' },
{ 'Name': 'Ivory Coast', 'Code': 'CIV', 'Flag': 'ci.png' },
{ 'Name': 'Jamaica', 'Code': 'JAM', 'Flag': 'jm.png' },
{ 'Name': 'Japan', 'Code': 'JPN', 'Flag': 'jp.png' },
{ 'Name': 'Jersey', 'Code': 'JEY', 'Flag': 'je.png' },
{ 'Name': 'Jordan', 'Code': 'JOR', 'Flag': 'jo.png' },
{ 'Name': 'Kazakhstan', 'Code': 'KAZ', 'Flag': 'kz.png' },
{ 'Name': 'Kenya', 'Code': 'KEN', 'Flag': 'ke.png' },
{ 'Name': 'Kiribati', 'Code': 'KIR', 'Flag': 'ki.png' },
{ 'Name': 'Kosovo', 'Code': 'XKX', 'Flag': 'xk.png' },
{ 'Name': 'Kuwait', 'Code': 'KWT', 'Flag': 'kw.png' },
{ 'Name': 'Kyrgyzstan', 'Code': 'KGZ', 'Flag': 'kg.png' },
{ 'Name': 'Laos', 'Code': 'LAO', 'Flag': 'la.png' },
{ 'Name': 'Latvia', 'Code': 'LVA', 'Flag': 'lv.png' },
{ 'Name': 'Lebanon', 'Code': 'LBN', 'Flag': 'lb.png' },
{ 'Name': 'Lesotho', 'Code': 'LSO', 'Flag': 'ls.png' },
{ 'Name': 'Liberia', 'Code': 'LBR', 'Flag': 'lr.png' },
{ 'Name': 'Libya', 'Code': 'LBY', 'Flag': 'ly.png' },
{ 'Name': 'Liechtenstein', 'Code': 'LIE', 'Flag': 'li.png' },
{ 'Name': 'Lithuania', 'Code': 'LTU', 'Flag': 'lt.png' },
{ 'Name': 'Luxembourg', 'Code': 'LUX', 'Flag': 'lu.png' },
{ 'Name': 'Macau', 'Code': 'MAC', 'Flag': 'mo.png' },
{ 'Name': 'Macedonia', 'Code': 'MKD', 'Flag': 'mk.png' },
{ 'Name': 'Madagascar', 'Code': 'MDG', 'Flag': 'mg.png' },
{ 'Name': 'Malawi', 'Code': 'MWI', 'Flag': 'mw.png' },
{ 'Name': 'Malaysia', 'Code': 'MYS', 'Flag': 'my.png' },
{ 'Name': 'Maldives', 'Code': 'MDV', 'Flag': 'mv.png' },
{ 'Name': 'Mali', 'Code': 'MLI', 'Flag': 'ml.png' },
{ 'Name': 'Malta', 'Code': 'MLT', 'Flag': 'mt.png' },
{ 'Name': 'Marshall Islands', 'Code': 'MHL', 'Flag': 'mh.png' },
{ 'Name': 'Mauritania', 'Code': 'MRT', 'Flag': 'mr.png' },
{ 'Name': 'Mauritius', 'Code': 'MUS', 'Flag': 'mu.png' },
{ 'Name': 'Mayotte', 'Code': 'MYT', 'Flag': 'yt.png' },
{ 'Name': 'Mexico', 'Code': 'MEX', 'Flag': 'mx.png' },
{ 'Name': 'Micronesia', 'Code': 'FSM', 'Flag': 'fm.png' },
{ 'Name': 'Moldova', 'Code': 'MDA', 'Flag': 'md.png' },
{ 'Name': 'Monaco', 'Code': 'MCO', 'Flag': 'mc.png' },
{ 'Name': 'Mongolia', 'Code': 'MNG', 'Flag': 'mn.png' },
{ 'Name': 'Montenegro', 'Code': 'MNE', 'Flag': 'me.png' },
{ 'Name': 'Montserrat', 'Code': 'MSR', 'Flag': 'ms.png' },
{ 'Name': 'Morocco', 'Code': 'MAR', 'Flag': 'ma.png' },
{ 'Name': 'Mozambique', 'Code': 'MOZ', 'Flag': 'mz.png' },
{ 'Name': 'Myanmar', 'Code': 'MMR', 'Flag': 'mm.png' },
{ 'Name': 'Namibia', 'Code': 'NAM', 'Flag': 'na.png' },
{ 'Name': 'Nauru', 'Code': 'NRU', 'Flag': 'nr.png' },
{ 'Name': 'Nepal', 'Code': 'NPL', 'Flag': 'np.png' },
{ 'Name': 'Netherlands', 'Code': 'NLD', 'Flag': 'nl.png' },
{ 'Name': 'Netherlands Antilles', 'Code': 'ANT', 'Flag': 'an.png' },
{ 'Name': 'New Caledonia', 'Code': 'NCL', 'Flag': 'nc.png' },
{ 'Name': 'New Zealand', 'Code': 'NZL', 'Flag': 'nz.png' },
{ 'Name': 'Nicaragua', 'Code': 'NIC', 'Flag': 'ni.png' },
{ 'Name': 'Niger', 'Code': 'NER', 'Flag': 'ne.png' },
{ 'Name': 'Nigeria', 'Code': 'NGA', 'Flag': 'ng.png' },
{ 'Name': 'Niue', 'Code': 'NIU', 'Flag': 'nu.png' },
{ 'Name': 'North Korea', 'Code': 'PRK', 'Flag': 'kp.png' },
{ 'Name': 'Northern Mariana Islands', 'Code': 'MNP', 'Flag': 'mp.png' },
{ 'Name': 'Norway', 'Code': 'NOR', 'Flag': 'no.png' },
{ 'Name': 'Oman', 'Code': 'OMN', 'Flag': 'om.png' },
{ 'Name': 'Pakistan', 'Code': 'PAK', 'Flag': 'pk.png' },
{ 'Name': 'Palau', 'Code': 'PLW', 'Flag': 'pw.png' },
{ 'Name': 'Palestine', 'Code': 'PSE', 'Flag': 'ps.png' },
{ 'Name': 'Panama', 'Code': 'PAN', 'Flag': 'pa.png' },
{ 'Name': 'Papua New Guinea', 'Code': 'PNG', 'Flag': 'pg.png' },
{ 'Name': 'Paraguay', 'Code': 'PRY', 'Flag': 'py.png' },
{ 'Name': 'Peru', 'Code': 'PER', 'Flag': 'pe.png' },
{ 'Name': 'Philippines', 'Code': 'PHL', 'Flag': 'ph.png' },
{ 'Name': 'Pitcairn', 'Code': 'PCN', 'Flag': 'pn.png' },
{ 'Name': 'Poland', 'Code': 'POL', 'Flag': 'pl.png' },
{ 'Name': 'Portugal', 'Code': 'PRT', 'Flag': 'pt.png' },
{ 'Name': 'Puerto Rico', 'Code': 'PRI', 'Flag': 'pr.png' },
{ 'Name': 'Qatar', 'Code': 'QAT', 'Flag': 'qa.png' },
{ 'Name': 'Republic of the Congo', 'Code': 'COG', 'Flag': 'cg.png' },
{ 'Name': 'Reunion', 'Code': 'REU', 'Flag': 're.png' },
{ 'Name': 'Romania', 'Code': 'ROU', 'Flag': 'ro.png' },
{ 'Name': 'Russia', 'Code': 'RUS', 'Flag': 'ru.png' },
{ 'Name': 'Rwanda', 'Code': 'RWA', 'Flag': 'rw.png' },
{ 'Name': 'Saint Barthelemy', 'Code': 'BLM', 'Flag': 'bl.png' },
{ 'Name': 'Saint Helena', 'Code': 'SHN', 'Flag': 'sh.png' },
{ 'Name': 'Saint Kitts_and_Nevis', 'Code': 'KNA', 'Flag': 'kn.png' },
{ 'Name': 'Saint Lucia', 'Code': 'LCA', 'Flag': 'lc.png' },
{ 'Name': 'Saint Martin', 'Code': 'MAF', 'Flag': 'mf.png' },
{ 'Name': 'Saint Pierre and Miquelon', 'Code': 'SPM', 'Flag': 'pm.png' },
{ 'Name': 'Saint Vincent and the Grenadines', 'Code': 'VCT', 'Flag': 'vc.png' },
{ 'Name': 'Samoa', 'Code': 'WSM', 'Flag': 'ws.png' },
{ 'Name': 'San Marino', 'Code': 'SMR', 'Flag': 'sm.png' },
{ 'Name': 'Sao Tome and Principe', 'Code': 'STP', 'Flag': 'st.png' },
{ 'Name': 'Saudi Arabia', 'Code': 'SAU', 'Flag': 'sa.png' },
{ 'Name': 'Senegal', 'Code': 'SEN', 'Flag': 'sn.png' },
{ 'Name': 'Serbia', 'Code': 'SRB', 'Flag': 'rs.png' },
{ 'Name': 'Seychelles', 'Code': 'SYC', 'Flag': 'sc.png' },
{ 'Name': 'Sierra Leone', 'Code': 'SLE', 'Flag': 'sl.png' },
{ 'Name': 'Singapore', 'Code': 'SGP', 'Flag': 'sg.png' },
{ 'Name': 'Sint Maarten', 'Code': 'SXM', 'Flag': 'sx.png' },
{ 'Name': 'Slovakia', 'Code': 'SVK', 'Flag': 'sk.png' },
{ 'Name': 'Slovenia', 'Code': 'SVN', 'Flag': 'si.png' },
{ 'Name': 'Solomon Islands', 'Code': 'SLB', 'Flag': 'sb.png' },
{ 'Name': 'Somalia', 'Code': 'SOM', 'Flag': 'so.png' },
{ 'Name': 'South Africa', 'Code': 'ZAF', 'Flag': 'za.png' },
{ 'Name': 'South Korea', 'Code': 'KOR', 'Flag': 'kr.png' },
{ 'Name': 'South Sudan', 'Code': 'SSD', 'Flag': 'ss.png' },
{ 'Name': 'Spain', 'Code': 'ESP', 'Flag': 'es.png' },
{ 'Name': 'Sri Lanka', 'Code': 'LKA', 'Flag': 'lk.png' },
{ 'Name': 'Sudan', 'Code': 'SDN', 'Flag': 'sd.png' },
{ 'Name': 'Suriname', 'Code': 'SUR', 'Flag': 'sr.png' },
{ 'Name': 'Svalbard and Jan Mayen', 'Code': 'SJM', 'Flag': 'sj.png' },
{ 'Name': 'Swaziland', 'Code': 'SWZ', 'Flag': 'sz.png' },
{ 'Name': 'Sweden', 'Code': 'SWE', 'Flag': 'se.png' },
{ 'Name': 'Switzerland', 'Code': 'CHE', 'Flag': 'ch.png' },
{ 'Name': 'Syria', 'Code': 'SYR', 'Flag': 'sy.png' },
{ 'Name': 'Taiwan', 'Code': 'TWN', 'Flag': 'tw.png' },
{ 'Name': 'Tajikistan', 'Code': 'TJK', 'Flag': 'tj.png' },
{ 'Name': 'Tanzania', 'Code': 'TZA', 'Flag': 'tz.png' },
{ 'Name': 'Thailand', 'Code': 'THA', 'Flag': 'th.png' },
{ 'Name': 'Togo', 'Code': 'TGO', 'Flag': 'tg.png' },
{ 'Name': 'Tokelau', 'Code': 'TKL', 'Flag': 'tk.png' },
{ 'Name': 'Tonga', 'Code': 'TON', 'Flag': 'to.png' },
{ 'Name': 'Trinidad and Tobago', 'Code': 'TTO', 'Flag': 'tt.png' },
{ 'Name': 'Tunisia', 'Code': 'TUN', 'Flag': 'tn.png' },
{ 'Name': 'Turkey', 'Code': 'TUR', 'Flag': 'tr.png' },
{ 'Name': 'Turkmenistan', 'Code': 'TKM', 'Flag': 'tm.png' },
{ 'Name': 'Turks and Caicos Islands', 'Code': 'TCA', 'Flag': 'tc.png' },
{ 'Name': 'Tuvalu', 'Code': 'TUV', 'Flag': 'tv.png' },
{ 'Name': 'U.S.Virgin Islands', 'Code': 'VIR', 'Flag': 'vi.png' },
{ 'Name': 'Uganda', 'Code': 'UGA', 'Flag': 'ug.png' },
{ 'Name': 'Ukraine', 'Code': 'UKR', 'Flag': 'ua.png' },
{ 'Name': 'United Arab Emirates', 'Code': 'ARE', 'Flag': 'ae.png' },
{ 'Name': 'United Kingdom', 'Code': 'GBR', 'Flag': 'gb.png' },
{ 'Name': 'United States', 'Code': 'USA', 'Flag': 'us.png' },
{ 'Name': 'Uruguay', 'Code': 'URY', 'Flag': 'uy.png' },
{ 'Name': 'Uzbekistan', 'Code': 'UZB', 'Flag': 'uz.png' },
{ 'Name': 'Vanuatu', 'Code': 'VUT', 'Flag': 'vu.png' },
{ 'Name': 'Vatican', 'Code': 'VAT', 'Flag': 'va.png' },
{ 'Name': 'Venezuela', 'Code': 'VEN', 'Flag': 've.png' },
{ 'Name': 'Vietnam', 'Code': 'VNM', 'Flag': 'vn.png' },
{ 'Name': 'Wallis and Futuna', 'Code': 'WLF', 'Flag': 'wf.png' },
{ 'Name': 'Western Sahara', 'Code': 'ESH', 'Flag': 'eh.png' },
{ 'Name': 'Yemen', 'Code': 'YEM', 'Flag': 'ye.png' },
{ 'Name': 'Zambia', 'Code': 'ZMB', 'Flag': 'zm.png' },
{ 'Name': 'Zimbabwe', 'Code': 'ZWE', 'Flag': 'zw.png' }]


class SearchButton extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            countryNames: countries,
            isSearched: false,
            selection:this.props.selection,
        };
    }

    render() {
        if (!this.state.isSearched) {
            return (
                <div>
                    <form action="http://localhost:9999/dashboard" method="post">
                        <label>Choose a country</label>
                        <select name="searched_countries">
                            {this.state.countryNames.map((country) => <option value={country.Code}>{country.Name}</option>)}
                        </select>
                        <p><input type="submit" onClick={this.setState({ isSearched: true })} name="submit" value="Submit"></input></p>
                    </form>
                </div>
            )
        } else {
            return (
                <div>
                    <form action="http://localhost:9999/dashboard" method="post">
                        <label>Choose a country</label>
                        <select name="searched_countries" onChange={this.state.selection}>
                            {this.state.countryNames.map((country) => <option value={country.Code}>{country.Name}</option>)}
                        </select>
                        <p><input type="submit" name="submit" value="Submit"></input></p>
                    </form>
                </div>
            );
        }
    }
}

class RankingTopThree extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isLoaded: false,
            rankings: [],
        };
    }


    render() {
        if (!this.state.isLoaded) {
            fetch("dashboard/ranking")
                .then(response => response.json())
                .then(response => this.setState({ rankings: response, isLoaded: true }));
        }
        return (
            <div>
                <p>
                    {this.state.rankings.map((country) => <p><img src={country.Flag} /></p>)}
                </p>
            </div>
        );
    }
}

class ImageComponent extends React.Component {
    render() {
        return (
            <div>
                <img src={this.props.imgFile} />
            </div>
        );
    }
}

class App extends React.Component {
    render() {
        return (
            <div>
                <SearchButton selection={this.props.selection}/>
                <ImageComponent imgFile={this.props.imgFile} />
                <RankingTopThree />
            </div>
        );
    }
}

ReactDOM.render(<App imgFile={data.imgFile} selection={data.selection} />, document.getElementById('image'))