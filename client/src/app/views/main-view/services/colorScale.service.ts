import { Injectable } from "@angular/core";

import * as d3 from 'd3';

@Injectable({
    providedIn: 'root'
})
export class ColorScaleService {

    public textColorScale: d3.ScaleSequential<any> = d3.scaleSequential([0, 1], d3.interpolateBlues);

}